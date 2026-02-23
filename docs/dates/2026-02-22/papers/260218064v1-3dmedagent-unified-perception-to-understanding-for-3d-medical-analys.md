---
layout: default
title: 3DMedAgent: Unified Perception-to-Understanding for 3D Medical Analysis
---

# 3DMedAgent: Unified Perception-to-Understanding for 3D Medical Analysis
**arXiv**：[2602.18064v1](https://arxiv.org/abs/2602.18064) · [PDF](https://arxiv.org/pdf/2602.18064.pdf)  
**作者**：Ziyue Wang, Linghan Cai, Chang Han Low, Haofeng Liu, Junde Wu, Jingyu Wang, Rui Wang, Lei Song, Jiang Bian, Jingjing Fu, Yueming Jin  

**一句话要点**：提出3DMedAgent，使2D多模态大语言模型无需3D微调即可执行3D CT分析，实现从感知到理解的统一处理。

**关键词**：3D医学分析, 多模态大语言模型, CT影像处理, 感知到理解, 结构化记忆, 工具协调

## 3 点简述
- 现有3D医学分析方法多为孤立任务建模或任务无关端到端范式，阻碍了感知证据的系统积累。
- 3DMedAgent通过协调异构视觉和文本工具，将复杂3D分析分解为从全局到局部、从3D体积到2D切片、从视觉证据到文本表示的可处理子任务。
- 在超过40个任务上的实验表明，3DMedAgent优于通用、医学和3D特定多模态大语言模型，并引入了DeepChestVQA基准进行评估。

## 摘要（原文）

> 3D CT analysis spans a continuum from low-level perception to high-level clinical understanding. Existing 3D-oriented analysis methods adopt either isolated task-specific modeling or task-agnostic end-to-end paradigms to produce one-hop outputs, impeding the systematic accumulation of perceptual evidence for downstream reasoning. In parallel, recent multimodal large language models (MLLMs) exhibit improved visual perception and can integrate visual and textual information effectively, yet their predominantly 2D-oriented designs fundamentally limit their ability to perceive and analyze volumetric medical data. To bridge this gap, we propose 3DMedAgent, a unified agent that enables 2D MLLMs to perform general 3D CT analysis without 3D-specific fine-tuning. 3DMedAgent coordinates heterogeneous visual and textual tools through a flexible MLLM agent, progressively decomposing complex 3D analysis into tractable subtasks that transition from global to regional views, from 3D volumes to informative 2D slices, and from visual evidence to structured textual representations. Central to this design, 3DMedAgent maintains a long-term structured memory that aggregates intermediate tool outputs and supports query-adaptive, evidence-driven multi-step reasoning. We further introduce the DeepChestVQA benchmark for evaluating unified perception-to-understanding capabilities in 3D thoracic imaging. Experiments across over 40 tasks demonstrate that 3DMedAgent consistently outperforms general, medical, and 3D-specific MLLMs, highlighting a scalable path toward general-purpose 3D clinical assistants.Code and data are available at \href{https://github.com/jinlab-imvr/3DMedAgent}{https://github.com/jinlab-imvr/3DMedAgent}.

