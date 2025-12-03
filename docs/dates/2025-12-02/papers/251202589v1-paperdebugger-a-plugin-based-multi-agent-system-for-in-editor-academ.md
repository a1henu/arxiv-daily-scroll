---
layout: default
title: PaperDebugger: A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing
---

# PaperDebugger: A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing
**arXiv**：[2512.02589v1](https://arxiv.org/abs/2512.02589) · [PDF](https://arxiv.org/pdf/2512.02589.pdf)  
**作者**：Junyi Hou, Andre Lin Huikai, Nuo Chen, Yiwei Gong, Bingsheng He  

**一句话要点**：提出PaperDebugger插件式多智能体系统，以在LaTeX编辑器内实现LLM驱动的学术写作辅助

**关键词**：学术写作助手, 多智能体系统, LaTeX编辑器集成, 插件架构, 模型上下文协议

## 3 点简述
- 现有学术写作助手与编辑器分离，无法深度交互文档状态和结构
- 通过Chrome扩展、Kubernetes编排和MCP工具链，实现可靠同步、版本控制和多智能体调度
- 演示集成工作流，包括本地编辑、结构化审阅和并行执行，早期分析显示用户积极参与

## 摘要（原文）

> Large language models are increasingly embedded into academic writing workflows, yet existing assistants remain external to the editor, preventing deep interaction with document state, structure, and revision history. This separation makes it impossible to support agentic, context-aware operations directly within LaTeX editors such as Overleaf. We present PaperDebugger, an in-editor, multi-agent, and plugin-based academic writing assistant that brings LLM-driven reasoning directly into the writing environment. Enabling such in-editor interaction is technically non-trivial: it requires reliable bidirectional synchronization with the editor, fine-grained version control and patching, secure state management, multi-agent scheduling, and extensible communication with external tools. PaperDebugger addresses these challenges through a Chrome-approved extension, a Kubernetes-native orchestration layer, and a Model Context Protocol (MCP) toolchain that integrates literature search, reference lookup, document scoring, and revision pipelines. Our demo showcases a fully integrated workflow, including localized edits, structured reviews, parallel agent execution, and diff-based updates, encapsulated within a minimal-intrusion user interface (UI). Early aggregated analytics demonstrate active user engagement and validate the practicality of an editor-native, agentic writing assistant. More details about this demo and video could be found at https://github.com/PaperDebugger/PaperDebugger.

