---
layout: default
title: K-MaT: Knowledge-Anchored Manifold Transport for Cross-Modal Prompt Learning in Medical Imaging
---

# K-MaT: Knowledge-Anchored Manifold Transport for Cross-Modal Prompt Learning in Medical Imaging
**arXiv**：[2603.06340v1](https://arxiv.org/abs/2603.06340) · [PDF](https://arxiv.org/pdf/2603.06340.pdf)  
**作者**：Jiajun Zeng, Shadi Albarqouni  

**一句话要点**：提出K-MaT框架，通过知识锚定和流形传输解决医学影像跨模态提示学习中的模态崩溃问题。

**关键词**：医学影像分析, 跨模态学习, 提示学习, 最优传输, 视觉语言模型, 零样本迁移

## 3 点简述
- 核心问题：大规模生物医学视觉语言模型从高端影像迁移到低端模态时易陷入模态特定捷径，导致性能崩溃。
- 方法要点：分解提示并锚定到临床文本描述，使用融合Gromov-Wasserstein最优传输对齐低端与高端提示流形。
- 实验或效果：在四个跨模态基准测试中实现SOTA，平均调和准确率提升至44.1%，在乳腺成像任务中缓解灾难性遗忘。

## 摘要（原文）

> Large-scale biomedical vision-language models (VLMs) adapted on high-end imaging (e.g., CT) often fail to transfer to frontline low-end modalities (e.g., radiography), collapsing into modality-specific shortcuts. We propose K-MaT (Knowledge-Anchored Manifold Transport), a prompt-learning framework that transfers decision structures to low-end modalities without requiring low-end training images. K-MaT factorizes prompts, anchors them to clinical text descriptions, and aligns the low-end prompt manifold to the visually-grounded high-end space using Fused Gromov-Wasserstein optimal transport. We evaluate K-MaT on four cross-modal benchmarks, including dermoscopy, mammography to ultrasound, and CT to chest X-ray. K-MaT achieves state-of-the-art results, improving the average harmonic mean of accuracy to 44.1% (from BiomedCoOp's 42.0%) and macro-F1 to 36.2%. Notably, on the challenging breast imaging task, it mitigates the catastrophic forgetting seen in standard methods like CoOp (which drops to 27.0% accuracy on the low-end), preserving robust performance across modalities. Aligning prompt manifolds via optimal transport provides a highly effective route for the zero-shot cross-modal deployment of medical VLMs.

