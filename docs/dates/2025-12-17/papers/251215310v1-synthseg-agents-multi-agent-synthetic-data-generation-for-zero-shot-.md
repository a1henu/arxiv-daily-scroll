---
layout: default
title: SynthSeg-Agents: Multi-Agent Synthetic Data Generation for Zero-Shot Weakly Supervised Semantic Segmentation
---

# SynthSeg-Agents: Multi-Agent Synthetic Data Generation for Zero-Shot Weakly Supervised Semantic Segmentation
**arXiv**：[2512.15310v1](https://arxiv.org/abs/2512.15310) · [PDF](https://arxiv.org/pdf/2512.15310.pdf)  
**作者**：Wangyu Wu, Zhenhong Chen, Xiaowei Huang, Fei Ma, Jimin Xiao  

**一句话要点**：提出SynthSeg-Agents多智能体框架，以解决零样本弱监督语义分割中无真实图像训练数据的问题。

**关键词**：零样本弱监督语义分割, 多智能体框架, 合成数据生成, 大型语言模型, 视觉语言模型, CLIP评分

## 3 点简述
- 核心问题：零样本弱监督语义分割需像素级预测，但现有方法依赖真实图像训练数据。
- 方法要点：采用自优化提示智能体和图像生成智能体，基于LLM和VLM生成高质量合成数据。
- 实验或效果：在PASCAL VOC 2012和COCO 2014上实现竞争性性能，无需真实训练图像。

## 摘要（原文）

> Weakly Supervised Semantic Segmentation (WSSS) with image level labels aims to produce pixel level predictions without requiring dense annotations. While recent approaches have leveraged generative models to augment existing data, they remain dependent on real world training samples. In this paper, we introduce a novel direction, Zero Shot Weakly Supervised Semantic Segmentation (ZSWSSS), and propose SynthSeg Agents, a multi agent framework driven by Large Language Models (LLMs) to generate synthetic training data entirely without real images. SynthSeg Agents comprises two key modules, a Self Refine Prompt Agent and an Image Generation Agent. The Self Refine Prompt Agent autonomously crafts diverse and semantically rich image prompts via iterative refinement, memory mechanisms, and prompt space exploration, guided by CLIP based similarity and nearest neighbor diversity filtering. These prompts are then passed to the Image Generation Agent, which leverages Vision Language Models (VLMs) to synthesize candidate images. A frozen CLIP scoring model is employed to select high quality samples, and a ViT based classifier is further trained to relabel the entire synthetic dataset with improved semantic precision. Our framework produces high quality training data without any real image supervision. Experiments on PASCAL VOC 2012 and COCO 2014 show that SynthSeg Agents achieves competitive performance without using real training images. This highlights the potential of LLM driven agents in enabling cost efficient and scalable semantic segmentation.

