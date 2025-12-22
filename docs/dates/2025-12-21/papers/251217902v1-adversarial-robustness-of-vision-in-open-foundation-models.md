---
layout: default
title: Adversarial Robustness of Vision in Open Foundation Models
---

# Adversarial Robustness of Vision in Open Foundation Models
**arXiv**：[2512.17902v1](https://arxiv.org/abs/2512.17902) · [PDF](https://arxiv.org/pdf/2512.17902.pdf)  
**作者**：Jonathon Fox, William J Buchanan, Pavlos Papadopoulos  

**一句话要点**：评估LLaVA-1.5-13B与Llama 3.2 Vision-8B-2在视觉对抗攻击下的鲁棒性

**关键词**：对抗鲁棒性, 视觉语言模型, PGD攻击, VQA评估, 开放权重模型

## 3 点简述
- 核心问题：视觉模态作为攻击向量对开放权重视觉语言模型性能的影响
- 方法要点：使用无目标PGD攻击视觉输入，在VQA v2数据集子集上评估
- 实验或效果：Llama 3.2 Vision在较高扰动水平下性能下降较小，对抗鲁棒性与基准性能不直接相关

## 摘要（原文）

> With the increase in deep learning, it becomes increasingly difficult to understand the model in which AI systems can identify objects. Thus, an adversary could aim to modify an image by adding unseen elements, which will confuse the AI in its recognition of an entity. This paper thus investigates the adversarial robustness of LLaVA-1.5-13B and Meta's Llama 3.2 Vision-8B-2. These are tested for untargeted PGD (Projected Gradient Descent) against the visual input modality, and empirically evaluated on the Visual Question Answering (VQA) v2 dataset subset. The results of these adversarial attacks are then quantified using the standard VQA accuracy metric. This evaluation is then compared with the accuracy degradation (accuracy drop) of LLaVA and Llama 3.2 Vision. A key finding is that Llama 3.2 Vision, despite a lower baseline accuracy in this setup, exhibited a smaller drop in performance under attack compared to LLaVA, particularly at higher perturbation levels. Overall, the findings confirm that the vision modality represents a viable attack vector for degrading the performance of contemporary open-weight VLMs, including Meta's Llama 3.2 Vision. Furthermore, they highlight that adversarial robustness does not necessarily correlate directly with standard benchmark performance and may be influenced by underlying architectural and training factors.

