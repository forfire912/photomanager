// Global state
let scannedFiles = [];
let duplicateGroups = [];

// Utility function to show results
function showResults(elementId, message, type = 'info') {
    const resultsDiv = document.getElementById(elementId);
    resultsDiv.innerHTML = message;
    resultsDiv.className = `results show ${type}`;
}

// Utility function to hide results
function hideResults(elementId) {
    const resultsDiv = document.getElementById(elementId);
    resultsDiv.className = 'results';
}

// Scan directories
async function scanDirectories() {
    const directoriesText = document.getElementById('directories').value.trim();
    const recursive = document.getElementById('recursive').checked;
    
    if (!directoriesText) {
        showResults('scan-results', '<strong>Error:</strong> Please enter at least one directory path.', 'error');
        return;
    }
    
    // Parse directories (one per line)
    const directories = directoriesText.split('\n')
        .map(d => d.trim())
        .filter(d => d.length > 0);
    
    showResults('scan-results', '<strong>Scanning...</strong> Please wait...', 'info');
    
    try {
        const response = await fetch('/api/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                directories: directories,
                recursive: recursive
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            scannedFiles = data.files;
            
            let message = `<h3>✓ Scan Complete</h3>`;
            message += `<p><strong>Total files found:</strong> ${data.total_files}</p>`;
            
            if (data.files.length > 0) {
                message += `<div class="file-list">`;
                data.files.slice(0, 50).forEach(file => {
                    message += `<div class="file-item">${file}</div>`;
                });
                if (data.files.length > 50) {
                    message += `<div class="file-item"><em>... and ${data.files.length - 50} more files</em></div>`;
                }
                message += `</div>`;
                
                // Enable find duplicates button
                document.getElementById('find-duplicates-btn').disabled = false;
                document.getElementById('preview-organize-btn').disabled = false;
                document.getElementById('execute-organize-btn').disabled = false;
            }
            
            showResults('scan-results', message, 'success');
        } else {
            showResults('scan-results', `<strong>Error:</strong> ${data.error}`, 'error');
        }
    } catch (error) {
        showResults('scan-results', `<strong>Error:</strong> ${error.message}`, 'error');
    }
}

// Find duplicates
async function findDuplicates() {
    if (scannedFiles.length === 0) {
        showResults('duplicate-results', '<strong>Error:</strong> Please scan directories first.', 'error');
        return;
    }
    
    showResults('duplicate-results', '<strong>Finding duplicates...</strong> Please wait...', 'info');
    
    try {
        const response = await fetch('/api/find-duplicates', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                files: scannedFiles
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            duplicateGroups = data.duplicate_groups;
            
            let message = `<h3>✓ Duplicate Detection Complete</h3>`;
            message += `<p><strong>Duplicate files found:</strong> ${data.total_duplicates} files in ${data.total_groups} groups</p>`;
            
            if (data.duplicate_groups.length > 0) {
                data.duplicate_groups.forEach((group, index) => {
                    message += `<div class="duplicate-group">`;
                    message += `<h4>Group ${index + 1} (${group.count} files)</h4>`;
                    message += `<ul class="duplicate-files">`;
                    group.files.forEach(file => {
                        message += `<li>${file}</li>`;
                    });
                    message += `</ul></div>`;
                });
                
                // Enable remove duplicates buttons
                document.getElementById('preview-remove-btn').disabled = false;
                document.getElementById('execute-remove-btn').disabled = false;
            } else {
                message += `<p>No duplicate files found! 🎉</p>`;
            }
            
            showResults('duplicate-results', message, 'success');
        } else {
            showResults('duplicate-results', `<strong>Error:</strong> ${data.error}`, 'error');
        }
    } catch (error) {
        showResults('duplicate-results', `<strong>Error:</strong> ${error.message}`, 'error');
    }
}

// Remove duplicates
async function removeDuplicates(execute) {
    if (duplicateGroups.length === 0) {
        showResults('remove-results', '<strong>Error:</strong> Please find duplicates first.', 'error');
        return;
    }
    
    const action = execute ? 'Removing duplicates...' : 'Previewing removal...';
    showResults('remove-results', `<strong>${action}</strong> Please wait...`, 'info');
    
    try {
        const response = await fetch('/api/remove-duplicates', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                duplicate_groups: duplicateGroups,
                execute: execute
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            let message = `<h3>✓ ${execute ? 'Removal' : 'Preview'} Complete</h3>`;
            
            if (data.dry_run) {
                message += `<p><strong>Would remove:</strong> ${data.removed_count} duplicate files</p>`;
                message += `<p class="info">This was a preview. Click "Execute Removal" to actually delete files.</p>`;
            } else {
                message += `<p><strong>Removed:</strong> ${data.removed_count} duplicate files</p>`;
                message += `<p class="info">Files have been permanently deleted.</p>`;
            }
            
            showResults('remove-results', message, 'success');
        } else {
            showResults('remove-results', `<strong>Error:</strong> ${data.error}`, 'error');
        }
    } catch (error) {
        showResults('remove-results', `<strong>Error:</strong> ${error.message}`, 'error');
    }
}

// Organize files
async function organizeFiles(execute) {
    if (scannedFiles.length === 0) {
        showResults('organize-results', '<strong>Error:</strong> Please scan directories first.', 'error');
        return;
    }
    
    const outputDir = document.getElementById('output-dir').value.trim();
    if (!outputDir) {
        showResults('organize-results', '<strong>Error:</strong> Please enter an output directory.', 'error');
        return;
    }
    
    const action = execute ? 'Organizing files...' : 'Previewing organization...';
    showResults('organize-results', `<strong>${action}</strong> Please wait...`, 'info');
    
    try {
        const response = await fetch('/api/organize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                files: scannedFiles,
                output_dir: outputDir,
                execute: execute
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            let message = `<h3>✓ ${execute ? 'Organization' : 'Preview'} Complete</h3>`;
            
            if (data.dry_run) {
                message += `<p><strong>Would organize:</strong> ${data.organized_count} files</p>`;
                message += `<p class="info">This was a preview. Click "Execute Organization" to actually organize files.</p>`;
            } else {
                message += `<p><strong>Organized:</strong> ${data.organized_count} files</p>`;
                message += `<p class="info">Files have been copied to: ${outputDir}</p>`;
            }
            
            showResults('organize-results', message, 'success');
        } else {
            showResults('organize-results', `<strong>Error:</strong> ${data.error}`, 'error');
        }
    } catch (error) {
        showResults('organize-results', `<strong>Error:</strong> ${error.message}`, 'error');
    }
}
