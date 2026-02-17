---
layout: default
title: EmbeWebAgent: Embedding Web Agents into Any Customized UI
---

# EmbeWebAgent: Embedding Web Agents into Any Customized UI
**arXiv**：[2602.14865v1](https://arxiv.org/abs/2602.14865) · [PDF](https://arxiv.org/pdf/2602.14865.pdf)  
**作者**：Chenyang Ma, Clyde Fare, Matthew Wilson, Dave Braines  

**一句话要点**：提出EmbeWebAgent框架，通过前端钩子和后端工作流在企业环境中嵌入定制UI的Web代理。

**关键词**：Web代理, 前端钩子, 后端工作流, 企业应用, UI嵌入, 混合粒度动作

## 3 点简述
- 核心问题：现有Web代理基于截图或DOM树操作，缺乏应用级访问，限制鲁棒性和动作表达能力。
- 方法要点：使用轻量前端钩子（如ARIA观察和WebSocket函数注册）和可重用后端工作流，实现栈无关的混合粒度动作。
- 实验或效果：演示显示最小改造工作，在实时UI设置中实现鲁棒的多步行为，支持导航、操作和领域分析。

## 摘要（原文）

> Most web agents operate at the human interface level, observing screenshots or raw DOM trees without application-level access, which limits robustness and action expressiveness. In enterprise settings, however, explicit control of both the frontend and backend is available. We present EmbeWebAgent, a framework for embedding agents directly into existing UIs using lightweight frontend hooks (curated ARIA and URL-based observations, and a per-page function registry exposed via a WebSocket) and a reusable backend workflow that performs reasoning and takes actions. EmbeWebAgent is stack-agnostic (e.g., React or Angular), supports mixed-granularity actions ranging from GUI primitives to higher-level composites, and orchestrates navigation, manipulation, and domain-specific analytics via MCP tools. Our demo shows minimal retrofitting effort and robust multi-step behaviors grounded in a live UI setting. Live Demo: https://youtu.be/Cy06Ljee1JQ

