---
layout: default
title: Revisiting Multi-Task Visual Representation Learning
---

# Revisiting Multi-Task Visual Representation Learning
**arXiv**：[2601.13886v1](https://arxiv.org/abs/2601.13886) · [PDF](https://arxiv.org/pdf/2601.13886.pdf)  
**作者**：Shangzhe Di, Zhonghua Zhai, Weidi Xie  

**一句话要点**：提出多任务视觉预训练框架MTV，整合视觉语言对比、自监督和密集空间目标以提升视觉表示学习。

**关键词**：多任务学习, 视觉表示学习, 伪标签生成, 密集空间监督, 视觉语言模型, 自监督学习

## 3 点简述
- 当前视觉表示学习存在分裂：视觉语言模型缺乏空间精度，自监督方法缺乏高层语义。
- MTV框架联合优化共享骨干网络，利用专家模型生成密集伪标签以减少人工标注需求。
- 实验表明MTV在空间推理和语义理解上取得最佳性能，并系统分析多任务学习机制。

## 摘要（原文）

> Current visual representation learning remains bifurcated: vision-language models (e.g., CLIP) excel at global semantic alignment but lack spatial precision, while self-supervised methods (e.g., MAE, DINO) capture intricate local structures yet struggle with high-level semantic context. We argue that these paradigms are fundamentally complementary and can be integrated into a principled multi-task framework, further enhanced by dense spatial supervision. We introduce MTV, a multi-task visual pretraining framework that jointly optimizes a shared backbone across vision-language contrastive, self-supervised, and dense spatial objectives. To mitigate the need for manual annotations, we leverage high-capacity "expert" models -- such as Depth Anything V2 and OWLv2 -- to synthesize dense, structured pseudo-labels at scale. Beyond the framework, we provide a systematic investigation into the mechanics of multi-task visual learning, analyzing: (i) the marginal gain of each objective, (ii) task synergies versus interference, and (iii) scaling behavior across varying data and model scales. Our results demonstrate that MTV achieves "best-of-both-worlds" performance, significantly enhancing fine-grained spatial reasoning without compromising global semantic understanding. Our findings suggest that multi-task learning, fueled by high-quality pseudo-supervision, is a scalable path toward more general visual encoders.

