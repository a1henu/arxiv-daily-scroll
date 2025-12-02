---
layout: default
title: SGDiff: Scene Graph Guided Diffusion Model for Image Collaborative SegCaptioning
---

# SGDiff: Scene Graph Guided Diffusion Model for Image Collaborative SegCaptioning
**arXiv**：[2512.01975v1](https://arxiv.org/abs/2512.01975) · [PDF](https://arxiv.org/pdf/2512.01975.pdf)  
**作者**：Xu Zhang, Jin Yuan, Hanwang Zhang, Guojin Zhong, Yongsheng Zang, Jiacheng Lin, Zhiyong Li  

**一句话要点**：提出SGDiff模型，利用场景图引导扩散过程，实现基于简单提示的图像协同分割与描述任务。

**关键词**：图像协同分割与描述, 场景图引导扩散模型, 多模态对齐, 可控图像理解, 扩散过程

## 3 点简述
- 核心问题：传统可控图像理解任务需高成本提示或输出有限，难以从简单提示生成多样语义结果。
- 方法要点：通过提示中心场景图适配器捕捉用户意图，结合场景图引导双模态Transformer预测对齐的掩码-描述对。
- 实验或效果：在两个数据集上验证，SGDiff在分割与描述任务中表现优异，以最小提示输入获得良好结果。

## 摘要（原文）

> Controllable image semantic understanding tasks, such as captioning or segmentation, necessitate users to input a prompt (e.g., text or bounding boxes) to predict a unique outcome, presenting challenges such as high-cost prompt input or limited information output. This paper introduces a new task ``Image Collaborative Segmentation and Captioning'' (SegCaptioning), which aims to translate a straightforward prompt, like a bounding box around an object, into diverse semantic interpretations represented by (caption, masks) pairs, allowing flexible result selection by users. This task poses significant challenges, including accurately capturing a user's intention from a minimal prompt while simultaneously predicting multiple semantically aligned caption words and masks. Technically, we propose a novel Scene Graph Guided Diffusion Model that leverages structured scene graph features for correlated mask-caption prediction. Initially, we introduce a Prompt-Centric Scene Graph Adaptor to map a user's prompt to a scene graph, effectively capturing his intention. Subsequently, we employ a diffusion process incorporating a Scene Graph Guided Bimodal Transformer to predict correlated caption-mask pairs by uncovering intricate correlations between them. To ensure accurate alignment, we design a Multi-Entities Contrastive Learning loss to explicitly align visual and textual entities by considering inter-modal similarity, resulting in well-aligned caption-mask pairs. Extensive experiments conducted on two datasets demonstrate that SGDiff achieves superior performance in SegCaptioning, yielding promising results for both captioning and segmentation tasks with minimal prompt input.

