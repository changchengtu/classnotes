/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.language = 'zh';
	config.extraPlugins = 'autosave';
	config.autosave_SaveKey = 'autosaveKey';
	config.autosave_NotOlderThan = 1;
	config.autosave_saveOnDestroy = false;
	config.autosaveTargetUrl = 'http://example.com/path_to_script_that_saves_data'; 
	
};
