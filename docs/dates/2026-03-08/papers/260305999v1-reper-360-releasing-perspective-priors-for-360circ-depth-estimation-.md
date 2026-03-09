---
layout: default
title: RePer-360: Releasing Perspective Priors for 360$^\circ$ Depth Estimation via Self-Modulation
---

# RePer-360: Releasing Perspective Priors for 360$^\circ$ Depth Estimation via Self-Modulation
**arXiv**：[2603.05999v1](https://arxiv.org/abs/2603.05999) · [PDF](https://arxiv.org/pdf/2603.05999.pdf)  
**作者**：Cheng Guan, Chunyu Lin, Zhijie Shen, Junsong Zhang, Jiyuan Wang  

**一句话要点**：提出RePer-360框架，通过自调制机制保留透视先验以解决360度图像深度估计的域适应问题。

**关键词**：360度深度估计, 域适应, 自调制, 几何对齐, 全景图像, 轻量级微调

## 3 点简述
- 核心问题：基于透视图像训练的深度基础模型在360度图像上泛化差，且全微调需大量全景数据。
- 方法要点：设计几何对齐引导模块和自条件AdaLN-Zero机制，实现轻量级全景域适应而不覆盖预训练知识。
- 实验或效果：仅用1%训练数据超越标准微调，相同域内训练设置下RMSE提升约20%。

## 摘要（原文）

> Recent depth foundation models trained on perspective imagery achieve strong performance, yet generalize poorly to 360$^\circ$ images due to the substantial geometric discrepancy between perspective and panoramic domains. Moreover, fully fine-tuning these models typically requires large amounts of panoramic data. To address this issue, we propose RePer-360, a distortion-aware self-modulation framework for monocular panoramic depth estimation that adapts depth foundation models while preserving powerful pretrained perspective priors. Specifically, we design a lightweight geometry-aligned guidance module to derive a modulation signal from two complementary projections (i.e., ERP and CP) and use it to guide the model toward the panoramic domain without overwriting its pretrained perspective knowledge. We further introduce a Self-Conditioned AdaLN-Zero mechanism that produces pixel-wise scaling factors to reduce the feature distribution gap between the perspective and panoramic domains. In addition, a cubemap-domain consistency loss further improves training stability and cross-projection alignment. By shifting the focus from complementary-projection fusion to panoramic domain adaptation under preserved pretrained perspective priors, RePer-360 surpasses standard fine-tuning methods while using only 1\% of the training data. Under the same in-domain training setting, it further achieves an approximately 20\% improvement in RMSE. Code will be released upon acceptance.

