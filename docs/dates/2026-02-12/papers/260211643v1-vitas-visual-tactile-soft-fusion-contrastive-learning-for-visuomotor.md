---
layout: default
title: ViTaS: Visual Tactile Soft Fusion Contrastive Learning for Visuomotor Learning
---

# ViTaS: Visual Tactile Soft Fusion Contrastive Learning for Visuomotor Learning
**arXiv**：[2602.11643v1](https://arxiv.org/abs/2602.11643) · [PDF](https://arxiv.org/pdf/2602.11643.pdf)  
**作者**：Yufeng Tian, Shuiqi Cheng, Tianming Wei, Tianxing Zhou, Yuanhang Zhang, Zixian Liu, Qianwei Han, Zhecheng Yuan, Huazhe Xu  

**一句话要点**：提出ViTaS框架，通过软融合对比学习和CVAE模块融合视觉与触觉信息以提升机器人操作性能。

**关键词**：视觉触觉融合, 对比学习, 机器人操作, 多模态学习, 遮挡处理

## 3 点简述
- 现有方法多直接拼接视觉与触觉特征，难以处理遮挡场景且未充分利用模态互补性。
- 引入软融合对比学习和CVAE模块，增强视觉-触觉表示的对齐与互补性。
- 在12个模拟和3个真实环境中验证，ViTaS显著优于现有基线方法。

## 摘要（原文）

> Tactile information plays a crucial role in human manipulation tasks and has recently garnered increasing attention in robotic manipulation. However, existing approaches mostly focus on the alignment of visual and tactile features and the integration mechanism tends to be direct concatenation. Consequently, they struggle to effectively cope with occluded scenarios due to neglecting the inherent complementary nature of both modalities and the alignment may not be exploited enough, limiting the potential of their real-world deployment. In this paper, we present ViTaS, a simple yet effective framework that incorporates both visual and tactile information to guide the behavior of an agent. We introduce Soft Fusion Contrastive Learning, an advanced version of conventional contrastive learning method and a CVAE module to utilize the alignment and complementarity within visuo-tactile representations. We demonstrate the effectiveness of our method in 12 simulated and 3 real-world environments, and our experiments show that ViTaS significantly outperforms existing baselines. Project page: https://skyrainwind.github.io/ViTaS/index.html.

