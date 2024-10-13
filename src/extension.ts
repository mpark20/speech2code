// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as path from 'path';
const WebSocket = require('ws');
import express from 'express';
import open from 'open';

const app = express();
const port = 9000;
const websocketPort = 9001;

app.use('/', express.static(path.join(__dirname, 'client')));
app.listen(port, () => {
	vscode.window.showInformationMessage(`[Speech to Text] Server running at localhost:${port}`);
	open(`http://localhost:${port}`);
});


// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "speech2code" is now active!');

	const wss = new WebSocket.Server({port: websocketPort});
	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	const disposable = vscode.commands.registerCommand('speech2code.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World from speech2code!');
		wss.on('connection', (socket: any) => {
			console.log('[Speech to Text] New WebSocket connection');
			vscode.window.showInformationMessage('[Speech to Text] New WebSocket connection');

			socket.on('message', (phrase: string) => {
				console.log(`[Speech to Text] New WebSocket message: ${phrase}`);
			});
		});
	});

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export function deactivate() {}
