---
layout: default
title: VENUS: Visual Editing with Noise Inversion Using Scene Graphs
---

# VENUS: Visual Editing with Noise Inversion Using Scene Graphs
**arXiv**：[2601.07219v1](https://arxiv.org/abs/2601.07219) · [PDF](https://arxiv.org/pdf/2601.07219.pdf)  
**作者**：Thanh-Nhan Vo, Trong-Thuan Nguyen, Tam V. Nguyen, Minh-Triet Tran  

**一句话要点**：提出VENUS框架，通过场景图和噪声反转实现免训练图像编辑，提升背景保留与语义一致性。

**关键词**：场景图编辑, 噪声反转, 免训练框架, 扩散模型, 图像编辑, 语义一致性

## 3 点简述
- 现有基于场景图的图像编辑方法依赖模型微调，计算成本高且可扩展性差。
- VENUS采用分割提示条件和噪声反转策略，分离编辑目标与背景，无需额外训练。
- 在PIE-Bench和EditVal基准上，VENUS显著提升PSNR、SSIM等指标，并大幅减少运行时间。

## 摘要（原文）

> State-of-the-art text-based image editing models often struggle to balance background preservation with semantic consistency, frequently resulting either in the synthesis of entirely new images or in outputs that fail to realize the intended edits. In contrast, scene graph-based image editing addresses this limitation by providing a structured representation of semantic entities and their relations, thereby offering improved controllability. However, existing scene graph editing methods typically depend on model fine-tuning, which incurs high computational cost and limits scalability. To this end, we introduce VENUS (Visual Editing with Noise inversion Using Scene graphs), a training-free framework for scene graph-guided image editing. Specifically, VENUS employs a split prompt conditioning strategy that disentangles the target object of the edit from its background context, while simultaneously leveraging noise inversion to preserve fidelity in unedited regions. Moreover, our proposed approach integrates scene graphs extracted from multimodal large language models with diffusion backbones, without requiring any additional training. Empirically, VENUS substantially improves both background preservation and semantic alignment on PIE-Bench, increasing PSNR from 22.45 to 24.80, SSIM from 0.79 to 0.84, and reducing LPIPS from 0.100 to 0.070 relative to the state-of-the-art scene graph editing model (SGEdit). In addition, VENUS enhances semantic consistency as measured by CLIP similarity (24.97 vs. 24.19). On EditVal, VENUS achieves the highest fidelity with a 0.87 DINO score and, crucially, reduces per-image runtime from 6-10 minutes to only 20-30 seconds. Beyond scene graph-based editing, VENUS also surpasses strong text-based editing baselines such as LEDIT++ and P2P+DirInv, thereby demonstrating consistent improvements across both paradigms.

