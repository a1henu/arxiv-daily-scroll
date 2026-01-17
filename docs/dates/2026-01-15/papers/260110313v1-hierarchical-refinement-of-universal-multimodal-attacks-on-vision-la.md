---
layout: default
title: Hierarchical Refinement of Universal Multimodal Attacks on Vision-Language Models
---

# Hierarchical Refinement of Universal Multimodal Attacks on Vision-Language Models
**arXiv**：[2601.10313v1](https://arxiv.org/abs/2601.10313) · [PDF](https://arxiv.org/pdf/2601.10313.pdf)  
**作者**：Peng-Fei Zhang, Zi Huang  

**一句话要点**：提出分层精炼攻击以解决视觉语言模型通用对抗攻击的样本依赖与优化不稳定问题

**关键词**：通用对抗攻击, 视觉语言模型, 分层精炼, 多模态攻击, 优化稳定性

## 3 点简述
- 现有攻击多为样本特定，计算开销大，限制了大规模应用
- HRA在样本和优化层面精炼通用扰动，包括图像解耦、ScMix增强和梯度层次优化
- 实验表明攻击在多种任务、模型和数据集上优于现有方法

## 摘要（原文）

> Existing adversarial attacks for VLP models are mostly sample-specific, resulting in substantial computational overhead when scaled to large datasets or new scenarios. To overcome this limitation, we propose Hierarchical Refinement Attack (HRA), a multimodal universal attack framework for VLP models. HRA refines universal adversarial perturbations (UAPs) at both the sample level and the optimization level. For the image modality, we disentangle adversarial examples into clean images and perturbations, allowing each component to be handled independently for more effective disruption of cross-modal alignment. We further introduce a ScMix augmentation strategy that diversifies visual contexts and strengthens both global and local utility of UAPs, thereby reducing reliance on spurious features. In addition, we refine the optimization path by leveraging a temporal hierarchy of historical and estimated future gradients to avoid local minima and stabilize universal perturbation learning. For the text modality, HRA identifies globally influential words by combining intra-sentence and inter-sentence importance measures, and subsequently utilizes these words as universal text perturbations. Extensive experiments across various downstream tasks, VLP models, and datasets demonstrate the superiority of the proposed universal multimodal attacks.

