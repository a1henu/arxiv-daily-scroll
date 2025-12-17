---
layout: default
title: SketchAssist: A Practical Assistant for Semantic Edits and Precise Local Redrawing
---

# SketchAssist: A Practical Assistant for Semantic Edits and Precise Local Redrawing
**arXiv**：[2512.14140v1](https://arxiv.org/abs/2512.14140) · [PDF](https://arxiv.org/pdf/2512.14140.pdf)  
**作者**：Han Zou, Yan Zhang, Ruiqi Yu, Cong Xie, Jie Huang, Zhenpeng Zhan  

**一句话要点**：提出SketchAssist助手，通过统一指令编辑与线条重绘解决线稿编辑中语义控制与结构保持的难题

**关键词**：线稿编辑, 语义编辑, 局部重绘, 可控生成, 专家混合, 交互式助手

## 3 点简述
- 现有系统难以在线稿编辑中同时支持高层语义修改与精确局部重绘，同时保持稀疏结构与风格
- 构建可控数据生成流程与统一编辑框架，通过任务引导的专家混合机制提升语义可控性与结构保真度
- 实验表明在指令遵循和风格/结构保持方面优于基线方法，实现了实用的线稿创作辅助

## 摘要（原文）

> Sketch editing is central to digital illustration, yet existing image editing systems struggle to preserve the sparse, style-sensitive structure of line art while supporting both high-level semantic changes and precise local redrawing. We present SketchAssist, an interactive sketch drawing assistant that accelerates creation by unifying instruction-guided global edits with line-guided region redrawing, while keeping unrelated regions and overall composition intact. To enable this assistant at scale, we introduce a controllable data generation pipeline that (i) constructs attribute-addition sequences from attribute-free base sketches, (ii) forms multi-step edit chains via cross-sequence sampling, and (iii) expands stylistic coverage with a style-preserving attribute-removal model applied to diverse sketches. Building on this data, SketchAssist employs a unified sketch editing framework with minimal changes to DiT-based editors. We repurpose the RGB channels to encode the inputs, enabling seamless switching between instruction-guided edits and line-guided redrawing within a single input interface. To further specialize behavior across modes, we integrate a task-guided mixture-of-experts into LoRA layers, routing by text and visual cues to improve semantic controllability, structural fidelity, and style preservation. Extensive experiments show state-of-the-art results on both tasks, with superior instruction adherence and style/structure preservation compared to recent baselines. Together, our dataset and SketchAssist provide a practical, controllable assistant for sketch creation and revision.

