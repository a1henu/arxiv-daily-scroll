---
layout: default
title: Synthetic Defect Image Generation for Power Line Insulator Inspection Using Multimodal Large Language Models
---

# Synthetic Defect Image Generation for Power Line Insulator Inspection Using Multimodal Large Language Models
**arXiv**：[2603.08069v1](https://arxiv.org/abs/2603.08069) · [PDF](https://arxiv.org/pdf/2603.08069.pdf)  
**作者**：Xuesong Wang, Caisheng Wang  

**一句话要点**：提出基于多模态大语言模型的合成缺陷图像生成方法，以解决电力线绝缘子缺陷分类中数据稀缺问题。

**关键词**：合成图像生成, 多模态大语言模型, 缺陷分类, 数据增强, 电力线绝缘子检测

## 3 点简述
- 核心问题：电力线绝缘子缺陷图像稀缺，导致缺陷分类器训练困难。
- 方法要点：使用现成多模态大语言模型，通过视觉参考和文本提示生成合成缺陷图像，并采用嵌入选择优化。
- 实验或效果：在低训练数据场景下，合成图像增强使测试F1分数从0.615提升至0.739，数据效率估计提高4-5倍。

## 摘要（原文）

> Utility companies increasingly rely on drone imagery for post-event and routine inspection, but training accurate defect-type classifiers remains difficult because defect examples are rare and inspection datasets are often limited or proprietary. We address this data-scarcity setting by using an off-the-shelf multimodal large language model (MLLM) as a training-free image generator to synthesize defect images from visual references and text prompts. Our pipeline increases diversity via dual-reference conditioning, improves label fidelity with lightweight human verification and prompt refinement, and filters the resulting synthetic pool using an embedding-based selection rule based on distances to class centroids computed from the real training split. We evaluate on ceramic insulator defect-type classification (shell vs. glaze) using a public dataset with a realistic low training-data regime (104 real training images; 152 validation; 308 test). Augmenting the 10% real training set with embedding-selected synthetic images improves test F1 score (harmonic mean of precision and recall) from 0.615 to 0.739 (20% relative), corresponding to an estimated 4--5x data-efficiency gain, and the gains persist with stronger backbone models and frozen-feature linear-probe baselines. These results suggest a practical, low-barrier path for improving defect recognition when collecting additional real defects is slow or infeasible.

