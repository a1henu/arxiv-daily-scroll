---
layout: default
title: Cross-Domain Transfer with Self-Supervised Spectral-Spatial Modeling for Hyperspectral Image Classification
---

# Cross-Domain Transfer with Self-Supervised Spectral-Spatial Modeling for Hyperspectral Image Classification
**arXiv**：[2601.18088v1](https://arxiv.org/abs/2601.18088) · [PDF](https://arxiv.org/pdf/2601.18088.pdf)  
**作者**：Jianshu Chao, Tianhua Lv, Qiqiong Ma, Yunfei Qiu, Li Fang, Huifang Shen, Wei Yao  

**一句话要点**：提出自监督跨域迁移框架，通过光谱-空间联合建模解决高光谱图像分类中的域适应问题。

**关键词**：自监督学习, 跨域迁移, 高光谱图像分类, 光谱-空间建模, 蒸馏训练

## 3 点简述
- 核心问题：现有方法依赖源域标注且易受分布偏移影响，导致跨域泛化性能下降。
- 方法要点：设计S2Former模块进行光谱-空间协同建模，并引入频率域约束增强细节感知能力。
- 实验或效果：在四个高光谱数据集上验证了稳定分类性能和强跨域适应性，适用于资源受限条件。

## 摘要（原文）

> Self-supervised learning has demonstrated considerable potential in hyperspectral representation, yet its application in cross-domain transfer scenarios remains under-explored. Existing methods, however, still rely on source domain annotations and are susceptible to distribution shifts, leading to degraded generalization performance in the target domain. To address this, this paper proposes a self-supervised cross-domain transfer framework that learns transferable spectral-spatial joint representations without source labels and achieves efficient adaptation under few samples in the target domain. During the self-supervised pre-training phase, a Spatial-Spectral Transformer (S2Former) module is designed. It adopts a dual-branch spatial-spectral transformer and introduces a bidirectional cross-attention mechanism to achieve spectral-spatial collaborative modeling: the spatial branch enhances structural awareness through random masking, while the spectral branch captures fine-grained differences. Both branches mutually guide each other to improve semantic consistency. We further propose a Frequency Domain Constraint (FDC) to maintain frequency-domain consistency through real Fast Fourier Transform (rFFT) and high-frequency magnitude loss, thereby enhancing the model's capability to discern fine details and boundaries. During the fine-tuning phase, we introduce a Diffusion-Aligned Fine-tuning (DAFT) distillation mechanism. This aligns semantic evolution trajectories through a teacher-student structure, enabling robust transfer learning under low-label conditions. Experimental results demonstrate stable classification performance and strong cross-domain adaptability across four hyperspectral datasets, validating the method's effectiveness under resource-constrained conditions.

