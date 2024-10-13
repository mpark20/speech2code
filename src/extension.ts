// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as path from 'path';

import { AssemblyAI, RealtimeTranscriber, RealtimeTranscript } from 'assemblyai'

// AssemblyAI configuration
const client = new AssemblyAI({
  apiKey: 'a8f8800503f64f2cb716dd36b090f909' 
})
const audioFile = 'https://assembly.ai/nbc.mp3'

const params = {
  audio: audioFile,
  speaker_labels: true
}

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	console.log('Congratulations, your extension "speech2code" is now active!');
	const disposable = vscode.commands.registerCommand('speech2code.helloWorld', async () => {
		vscode.window.showInformationMessage('Hello World from speech2code!');
		run();
	});
	context.subscriptions.push(disposable);
}

// Runs transcription
const run = async () => {
	const transcript = await client.transcripts.transcribe(params)

	if (transcript.status === 'error') {
		console.error(`Transcription failed: ${transcript.error}`)
		process.exit(1)
	}

	console.log(transcript.text)

	const editor = vscode.window.activeTextEditor;
	if (editor && typeof transcript.text === "string") {
		const position = editor.selection.active;  // Current cursor position
		const text: string = transcript.text
		editor.edit(editBuilder => {
			editBuilder.insert(position, text);  // Insert text at cursor position
		});
	}

	for (let utterance of transcript.utterances!) {
		console.log(`Speaker ${utterance.speaker}: ${utterance.text}`)
	}
}

// This method is called when your extension is deactivated
export function deactivate() {}
