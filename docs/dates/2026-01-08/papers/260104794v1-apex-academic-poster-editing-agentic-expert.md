---
layout: default
title: APEX: Academic Poster Editing Agentic Expert
---

# APEX: Academic Poster Editing Agentic Expert
**arXiv**：[2601.04794v1](https://arxiv.org/abs/2601.04794) · [PDF](https://arxiv.org/pdf/2601.04794.pdf)  
**作者**：Chengxin Shi, Qinnan Cai, Zeyuan Chen, Long Zeng, Yibo Zhao, Jing Yu, Jianxiang Yu, Xiang Li  

**一句话要点**：提出APEX交互式学术海报编辑框架，以解决现有方法无法满足复杂用户意图的问题。

**关键词**：学术海报编辑, 交互式框架, 多级API编辑, 基准构建, 视觉语言模型评估

## 3 点简述
- 核心问题：现有学术海报生成方法多为单次非交互式，难以对齐主观用户意图。
- 方法要点：APEX支持基于API的多级细粒度编辑和审阅调整机制，实现交互式控制。
- 实验或效果：在APEX-Bench基准上显著优于基线方法，评估涵盖指令完成度和视觉一致性。

## 摘要（原文）

> Designing academic posters is a labor-intensive process requiring the precise balance of high-density content and sophisticated layout. While existing paper-to-poster generation methods automate initial drafting, they are typically single-pass and non-interactive, often fail to align with complex, subjective user intent. To bridge this gap, we propose APEX (Academic Poster Editing agentic eXpert), the first agentic framework for interactive academic poster editing, supporting fine-grained control with robust multi-level API-based editing and a review-and-adjustment Mechanism. In addition, we introduce APEX-Bench, the first systematic benchmark comprising 514 academic poster editing instructions, categorized by a multi-dimensional taxonomy including operation type, difficulty, and abstraction level, constructed via reference-guided and reference-free strategies to ensure realism and diversity. We further establish a multi-dimensional VLM-as-a-judge evaluation protocol to assess instruction fulfillment, modification scope, and visual consistency & harmony. Experimental results demonstrate that APEX significantly outperforms baseline methods. Our implementation is available at https://github.com/Breesiu/APEX.

