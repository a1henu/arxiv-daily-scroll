---
layout: default
title: Revisiting the Role of Foundation Models in Cell-Level Histopathological Image Analysis under Small-Patch Constraints -- Effects of Training Data Scale and Blur Perturbations on CNNs and Vision Transformers
---

# Revisiting the Role of Foundation Models in Cell-Level Histopathological Image Analysis under Small-Patch Constraints -- Effects of Training Data Scale and Blur Perturbations on CNNs and Vision Transformers
**arXiv**：[2603.04081v1](https://arxiv.org/abs/2603.04081) · [PDF](https://arxiv.org/pdf/2603.04081.pdf)  
**作者**：Hiroki Kagiyama, Toru Nagasaka, Yukari Adachi, Takaaki Tachibana, Ryota Ito, Mitsugu Fujita, Kimihiro Yamashita, Yoshihiro Kakeji  

**一句话要点**：评估小尺寸病理图像分析中任务特定模型优于基础模型，强调数据规模与模糊鲁棒性

**关键词**：细胞级病理图像分析, 小尺寸图像分类, 基础模型评估, 数据规模效应, 模糊鲁棒性, Vision Transformer

## 3 点简述
- 核心问题：细胞级病理图像分析需处理极小图像块（40x40像素），基础模型在此约束下的有效性未知。
- 方法要点：系统比较任务特定模型与基础模型，通过多数据规模训练和模糊扰动测试评估性能。
- 实验或效果：任务特定模型随数据增加持续提升，基础模型在中等样本量饱和；自定义ViT精度最高且推理成本低。

## 摘要（原文）

> Background and objective: Cell-level pathological image analysis requires working with extremely small image patches (40x40 pixels), far below standard ImageNet resolutions. It remains unclear whether modern deep learning architectures and foundation models can learn robust and scalable representations under this constraint. We systematically evaluated architectural suitability and data-scale effects for small-patch cell classification. Methods: We analyzed 303 colorectal cancer specimens with CD103/CD8 immunostaining, generating 185,432 annotated cell images. Eight task-specific architectures were trained from scratch at multiple data scales (FlagLimit: 256--16,384 samples per class), and three foundation models were evaluated via linear probing and fine-tuning after resizing inputs to 224x224 pixels. Robustness to blur was assessed using pre- and post-resize Gaussian perturbations. Results: Task-specific models improved consistently with increasing data scale, whereas foundation models saturated at moderate sample sizes. A Vision Transformer optimized for small patches (CustomViT) achieved the highest accuracy, outperforming all foundation models with substantially lower inference cost. Blur robustness was comparable across architectures, with no qualitative advantage observed for foundation models. Conclusion: For cell-level classification under extreme spatial constraints, task-specific architectures are more effective and efficient than foundation models once sufficient training data are available. Higher clean accuracy does not imply superior robustness, and large pre-trained models offer limited benefit in the small-patch regime.

