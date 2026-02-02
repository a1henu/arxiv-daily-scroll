---
layout: default
title: Color Matters: Demosaicing-Guided Color Correlation Training for Generalizable AI-Generated Image Detection
---

# Color Matters: Demosaicing-Guided Color Correlation Training for Generalizable AI-Generated Image Detection
**arXiv**：[2601.22778v1](https://arxiv.org/abs/2601.22778) · [PDF](https://arxiv.org/pdf/2601.22778.pdf)  
**作者**：Nan Zhong, Yiran Xu, Mian Zou  

**一句话要点**：提出基于去马赛克引导的颜色相关性训练框架，以提升AI生成图像检测的泛化能力。

**关键词**：AI生成图像检测, 颜色相关性, 去马赛克, 泛化能力, 自监督学习, 相机成像管道

## 3 点简述
- 核心问题：现有基于生成伪影的检测器泛化性差，难以应对多样化的AI生成图像。
- 方法要点：利用相机成像管道的颜色相关性，通过模拟CFA采样和自监督U-Net建模条件分布。
- 实验或效果：在超过20个未见生成器上实现最优泛化和鲁棒性，显著超越先前方法。

## 摘要（原文）

> As realistic AI-generated images threaten digital authenticity, we address the generalization failure of generative artifact-based detectors by exploiting the intrinsic properties of the camera imaging pipeline. Concretely, we investigate color correlations induced by the color filter array (CFA) and demosaicing, and propose a Demosaicing-guided Color Correlation Training (DCCT) framework for AI-generated image detection. By simulating the CFA sampling pattern, we decompose each color image into a single-channel input (as the condition) and the remaining two channels as the ground-truth targets (for prediction). A self-supervised U-Net is trained to model the conditional distribution of the missing channels from the given one, parameterized via a mixture of logistic functions. Our theoretical analysis reveals that DCCT targets a provable distributional difference in color-correlation features between photographic and AI-generated images. By leveraging these distinct features to construct a binary classifier, DCCT achieves state-of-the-art generalization and robustness, significantly outperforming prior methods across over 20 unseen generators.

