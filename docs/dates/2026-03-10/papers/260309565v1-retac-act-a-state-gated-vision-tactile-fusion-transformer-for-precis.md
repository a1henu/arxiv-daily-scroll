---
layout: default
title: ReTac-ACT: A State-Gated Vision-Tactile Fusion Transformer for Precision Assembly
---

# ReTac-ACT: A State-Gated Vision-Tactile Fusion Transformer for Precision Assembly
**arXiv**：[2603.09565v1](https://arxiv.org/abs/2603.09565) · [PDF](https://arxiv.org/pdf/2603.09565.pdf)  
**作者**：Minchi Ruan, LiangQing Zhou, Hongtong Li, Zongtao Wang, ZhaoMing Lu, Jianwei Zhang, Bin Fang  

**一句话要点**：提出ReTac-ACT视觉-触觉融合Transformer，通过状态门控解决精密装配中视觉遮挡问题。

**关键词**：精密装配, 视觉-触觉融合, Transformer, 模仿学习, 状态门控, 触觉重建

## 3 点简述
- 核心问题：精密装配在‘最后一毫米’区域因视觉遮挡导致视觉反馈失效，需亚毫米级校正。
- 方法要点：采用双向交叉注意力、基于本体感知的门控网络和触觉重建目标，实现动态视觉-触觉特征融合。
- 实验或效果：在NIST装配任务板基准上达到90%成功率，0.1mm间隙下保持80%成功率，优于纯视觉基线。

## 摘要（原文）

> Precision assembly requires sub-millimeter corrections in contact-rich "last-millimeter" regions where visual feedback fails due to occlusion from the end-effector and workpiece. We present ReTac-ACT (Reconstruction-enhanced Tactile ACT), a vision-tactile imitation learning policy that addresses this challenge through three synergistic mechanisms: (i) bidirectional cross-attention enabling reciprocal visuo-tactile feature enhancement before fusion, (ii) a proprioception-conditioned gating network that dynamically elevates tactile reliance when visual occlusion occurs, and (iii) a tactile reconstruction objective enforcing learning of manipulation-relevant contact information rather than generic visual textures. Evaluated on the standardized NIST Assembly Task Board M1 benchmark, ReTac-ACT achieves 90% peg-in-hole success, substantially outperforming vision-only and generalist baseline methods, and maintains 80% success at industrial-grade 0.1mm clearance. Ablation studies validate that each architectural component is indispensable. The ReTac-ACT codebase and a vision-tactile demonstration dataset covering various clearance levels with both visual and tactile features will be released to support reproducible research.

