---
layout: default
title: Reg-TTR, Test-Time Refinement for Fast, Robust and Accurate Image Registration
---

# Reg-TTR, Test-Time Refinement for Fast, Robust and Accurate Image Registration
**arXiv**：[2601.19114v1](https://arxiv.org/abs/2601.19114) · [PDF](https://arxiv.org/pdf/2601.19114.pdf)  
**作者**：Lin Chen, Yue He, Fengting Zhang, Yaonan Wang, Fengming Lin, Xiang Chen, Min Liu  

**一句话要点**：提出Reg-TTR测试时精炼框架，结合深度学习和传统方法提升图像配准精度与速度

**关键词**：图像配准, 测试时精炼, 深度学习, 传统方法, 领域偏移, 推理速度

## 3 点简述
- 传统图像配准方法稳健但速度慢，深度学习快速但易受领域偏移影响
- Reg-TTR在推理时精炼预训练模型预测，融合深度学习和传统技术优势
- 实验显示精度达SOTA，额外推理时间仅21%（0.56秒），代码将开源

## 摘要（原文）

> Traditional image registration methods are robust but slow due to their iterative nature. While deep learning has accelerated inference, it often struggles with domain shifts. Emerging registration foundation models offer a balance of speed and robustness, yet typically cannot match the peak accuracy of specialized models trained on specific datasets. To mitigate this limitation, we propose Reg-TTR, a test-time refinement framework that synergizes the complementary strengths of both deep learning and conventional registration techniques. By refining the predictions of pre-trained models at inference, our method delivers significantly improved registration accuracy at a modest computational cost, requiring only 21% additional inference time (0.56s). We evaluate Reg-TTR on two distinct tasks and show that it achieves state-of-the-art (SOTA) performance while maintaining inference speeds close to previous deep learning methods. As foundation models continue to emerge, our framework offers an efficient strategy to narrow the performance gap between registration foundation models and SOTA methods trained on specialized datasets. The source code will be publicly available following the acceptance of this work.

