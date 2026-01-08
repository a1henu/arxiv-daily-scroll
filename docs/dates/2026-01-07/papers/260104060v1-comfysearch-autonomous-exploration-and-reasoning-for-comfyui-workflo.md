---
layout: default
title: ComfySearch: Autonomous Exploration and Reasoning for ComfyUI Workflows
---

# ComfySearch: Autonomous Exploration and Reasoning for ComfyUI Workflows
**arXiv**：[2601.04060v1](https://arxiv.org/abs/2601.04060) · [PDF](https://arxiv.org/pdf/2601.04060.pdf)  
**作者**：Jinwei Su, Qizhen Lan, Zeyu Wang, Yinghui Xia, Hairu Wen, Yiqun Duan, Xi Xiao, Tianyu Shi, Yang Jingsong, Lewei He  

**一句话要点**：提出ComfySearch以解决ComfyUI工作流生成中的探索与一致性难题

**关键词**：ComfyUI工作流生成, 自主探索, 验证引导构建, 图约束优化, 代理框架

## 3 点简述
- 核心问题：ComfyUI组件众多，严格图约束下长程结构一致性维护困难，导致工作流通过率低和质量受限。
- 方法要点：采用代理框架，通过验证引导的工作流构建，有效探索组件空间并生成功能管道。
- 实验或效果：在复杂创意任务上显著优于现有方法，实现更高执行率、解决方案率和更强泛化能力。

## 摘要（原文）

> AI-generated content has progressed from monolithic models to modular workflows, especially on platforms like ComfyUI, allowing users to customize complex creative pipelines. However, the large number of components in ComfyUI and the difficulty of maintaining long-horizon structural consistency under strict graph constraints frequently lead to low pass rates and workflows of limited quality. To tackle these limitations, we present ComfySearch, an agentic framework that can effectively explore the component space and generate functional ComfyUI pipelines via validation-guided workflow construction. Experiments demonstrate that ComfySearch substantially outperforms existing methods on complex and creative tasks, achieving higher executability (pass) rates, higher solution rates, and stronger generalization.

