#!/usr/bin/env python3
"""
Photo Manager Web UI - A web-based visualization interface for photo management
"""

import os
import json
from pathlib import Path
from flask import Flask, render_template, request, jsonify
from photo_manager import (
    scan_directory, find_duplicates, remove_duplicates, 
    organize_by_date, get_file_date, ALL_EXTENSIONS
)

app = Flask(__name__)


@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')


@app.route('/api/scan', methods=['POST'])
def api_scan():
    """Scan directories for media files"""
    data = request.json
    directories = data.get('directories', [])
    recursive = data.get('recursive', True)
    
    if not directories:
        return jsonify({'error': 'No directories provided'}), 400
    
    all_files = []
    for directory in directories:
        if not os.path.exists(directory):
            return jsonify({'error': f'Directory does not exist: {directory}'}), 400
        
        files = scan_directory(directory, recursive=recursive)
        all_files.extend(files)
    
    # Convert Path objects to strings
    file_list = [str(f) for f in all_files]
    
    return jsonify({
        'success': True,
        'total_files': len(file_list),
        'files': file_list
    })


@app.route('/api/find-duplicates', methods=['POST'])
def api_find_duplicates():
    """Find duplicate files"""
    data = request.json
    file_paths = data.get('files', [])
    
    if not file_paths:
        return jsonify({'error': 'No files provided'}), 400
    
    # Convert strings back to Path objects
    files = [Path(f) for f in file_paths]
    
    duplicates = find_duplicates(files)
    
    # Convert to serializable format
    duplicate_groups = []
    for file_hash, file_list in duplicates.items():
        duplicate_groups.append({
            'hash': file_hash,
            'files': [str(f) for f in file_list],
            'count': len(file_list)
        })
    
    total_duplicates = sum(len(files) - 1 for files in duplicates.values())
    
    return jsonify({
        'success': True,
        'duplicate_groups': duplicate_groups,
        'total_duplicates': total_duplicates,
        'total_groups': len(duplicate_groups)
    })


@app.route('/api/remove-duplicates', methods=['POST'])
def api_remove_duplicates():
    """Remove duplicate files"""
    data = request.json
    duplicate_groups = data.get('duplicate_groups', [])
    execute = data.get('execute', False)
    
    if not duplicate_groups:
        return jsonify({'error': 'No duplicate groups provided'}), 400
    
    # Convert back to the format expected by remove_duplicates
    duplicates = {}
    for group in duplicate_groups:
        file_hash = group['hash']
        files = [Path(f) for f in group['files']]
        duplicates[file_hash] = files
    
    removed_count = remove_duplicates(duplicates, dry_run=not execute)
    
    return jsonify({
        'success': True,
        'removed_count': removed_count,
        'dry_run': not execute
    })


@app.route('/api/organize', methods=['POST'])
def api_organize():
    """Organize files by date"""
    data = request.json
    file_paths = data.get('files', [])
    output_dir = data.get('output_dir', '')
    execute = data.get('execute', False)
    
    if not file_paths:
        return jsonify({'error': 'No files provided'}), 400
    
    if not output_dir:
        return jsonify({'error': 'No output directory provided'}), 400
    
    # Convert strings back to Path objects
    files = [Path(f) for f in file_paths]
    
    organized_count = organize_by_date(files, output_dir, dry_run=not execute)
    
    return jsonify({
        'success': True,
        'organized_count': organized_count,
        'dry_run': not execute
    })


@app.route('/api/file-info', methods=['POST'])
def api_file_info():
    """Get information about a specific file"""
    data = request.json
    file_path = data.get('file_path', '')
    
    if not file_path or not os.path.exists(file_path):
        return jsonify({'error': 'File does not exist'}), 400
    
    file_path = Path(file_path)
    file_date = get_file_date(file_path)
    file_size = os.path.getsize(file_path)
    
    return jsonify({
        'success': True,
        'file_path': str(file_path),
        'file_name': file_path.name,
        'file_size': file_size,
        'file_date': file_date.isoformat() if file_date else None,
        'extension': file_path.suffix.lower()
    })


def main():
    """Run the web application"""
    print("Starting Photo Manager Web UI...")
    print("Open your browser and navigate to: http://127.0.0.1:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
