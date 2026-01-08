---
layout: default
title: Adaptive Attention Distillation for Robust Few-Shot Segmentation under Environmental Perturbations
---

# Adaptive Attention Distillation for Robust Few-Shot Segmentation under Environmental Perturbations
**arXiv**：[2601.03596v1](https://arxiv.org/abs/2601.03596) · [PDF](https://arxiv.org/pdf/2601.03596.pdf)  
**作者**：Qianyu Guo, Jingrong Wu, Jieji Ren, Weifeng Ge, Wenqiang Zhang  

**一句话要点**：提出自适应注意力蒸馏方法，以增强少样本分割在环境扰动下的鲁棒性。

**关键词**：少样本分割, 环境鲁棒性, 注意力蒸馏, 语义对比, 基准数据集, 自适应学习

## 3 点简述
- 核心问题：现有少样本分割模型在复杂环境（如光照变化、运动模糊）下性能下降，难以满足实际部署需求。
- 方法要点：通过自适应注意力蒸馏，反复对比和提炼支持图像与查询图像间的共享语义，生成类别特定注意力。
- 实验或效果：在环境鲁棒少样本分割基准上，mIoU提升3.3%-8.5%，展现优越性能和强泛化能力。

## 摘要（原文）

> Few-shot segmentation (FSS) aims to rapidly learn novel class concepts from limited examples to segment specific targets in unseen images, and has been widely applied in areas such as medical diagnosis and industrial inspection. However, existing studies largely overlook the complex environmental factors encountered in real world scenarios-such as illumination, background, and camera viewpoint-which can substantially increase the difficulty of test images. As a result, models trained under laboratory conditions often fall short of practical deployment requirements. To bridge this gap, in this paper, an environment-robust FSS setting is introduced that explicitly incorporates challenging test cases arising from complex environments-such as motion blur, small objects, and camouflaged targets-to enhance model's robustness under realistic, dynamic conditions. An environment robust FSS benchmark (ER-FSS) is established, covering eight datasets across multiple real world scenarios. In addition, an Adaptive Attention Distillation (AAD) method is proposed, which repeatedly contrasts and distills key shared semantics between known (support) and unknown (query) images to derive class-specific attention for novel categories. This strengthens the model's ability to focus on the correct targets in complex environments, thereby improving environmental robustness. Comparative experiments show that AAD improves mIoU by 3.3% - 8.5% across all datasets and settings, demonstrating superior performance and strong generalization. The source code and dataset are available at: https://github.com/guoqianyu-alberta/Adaptive-Attention-Distillation-for-FSS.

