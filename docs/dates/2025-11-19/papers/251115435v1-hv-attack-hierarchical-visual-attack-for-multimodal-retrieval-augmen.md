---
layout: default
title: HV-Attack: Hierarchical Visual Attack for Multimodal Retrieval Augmented Generation
---

# HV-Attack: Hierarchical Visual Attack for Multimodal Retrieval Augmented Generation
**arXiv**：[2511.15435v1](https://arxiv.org/abs/2511.15435) · [PDF](https://arxiv.org/pdf/2511.15435.pdf)  
**作者**：Linyin Luo, Yujuan Ding, Yunshan Ma, Wenqi Fan, Hanjiang Lai  

**一句话要点**：提出分层视觉攻击以破坏多模态检索增强生成系统的生成能力

**关键词**：多模态检索增强生成, 视觉攻击, 对抗性扰动, 跨模态对齐, 生成器误导

## 3 点简述
- 核心问题：多模态检索增强生成系统易受仅图像输入的视觉攻击，无需篡改其他组件。
- 方法要点：设计分层两阶段策略，通过扰动图像输入使检索器召回无关知识，误导生成器。
- 实验或效果：在OK-VQA和InfoSeek数据集上验证，显著降低检索和生成性能。

## 摘要（原文）

> Advanced multimodal Retrieval-Augmented Generation (MRAG) techniques have been widely applied to enhance the capabilities of Large Multimodal Models (LMMs), but they also bring along novel safety issues. Existing adversarial research has revealed the vulnerability of MRAG systems to knowledge poisoning attacks, which fool the retriever into recalling injected poisoned contents. However, our work considers a different setting: visual attack of MRAG by solely adding imperceptible perturbations at the image inputs of users, without manipulating any other components. This is challenging due to the robustness of fine-tuned retrievers and large-scale generators, and the effect of visual perturbation may be further weakened by propagation through the RAG chain. We propose a novel Hierarchical Visual Attack that misaligns and disrupts the two inputs (the multimodal query and the augmented knowledge) of MRAG's generator to confuse its generation. We further design a hierarchical two-stage strategy to obtain misaligned augmented knowledge. We disrupt the image input of the retriever to make it recall irrelevant knowledge from the original database, by optimizing the perturbation which first breaks the cross-modal alignment and then disrupts the multimodal semantic alignment. We conduct extensive experiments on two widely-used MRAG datasets: OK-VQA and InfoSeek. We use CLIP-based retrievers and two LMMs BLIP-2 and LLaVA as generators. Results demonstrate the effectiveness of our visual attack on MRAG through the significant decrease in both retrieval and generation performance.

