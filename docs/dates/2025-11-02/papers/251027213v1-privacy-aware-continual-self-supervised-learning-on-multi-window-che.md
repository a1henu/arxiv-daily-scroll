---
layout: default
title: Privacy-Aware Continual Self-Supervised Learning on Multi-Window Chest Computed Tomography for Domain-Shift Robustness
---

# Privacy-Aware Continual Self-Supervised Learning on Multi-Window Chest Computed Tomography for Domain-Shift Robustness
**arXiv**：[2510.27213v1](https://arxiv.org/abs/2510.27213) · [PDF](https://arxiv.org/pdf/2510.27213.pdf)  
**作者**：Ren Tasai, Guang Li, Ren Togo, Takahiro Ogawa, Kenji Hirata, Minghui Tang, Takaaki Yoshimura, Hiroyuki Sugimori, Noriko Nishioka, Yukie Shimizu, Kohsuke Kudo, Miki Haseyama  

**一句话要点**：提出隐私感知持续自监督学习框架，以增强多窗口胸部CT的域偏移鲁棒性。

**关键词**：持续自监督学习, 域偏移鲁棒性, 隐私保护, 特征蒸馏, 胸部CT图像

## 3 点简述
- 核心问题：医疗图像诊断中域偏移和数据隐私限制模型泛化能力。
- 方法要点：结合潜在回放和特征蒸馏，缓解灾难性遗忘并保护隐私。
- 实验或效果：在胸部CT多窗口设置下验证，性能优于其他方法。

## 摘要（原文）

> We propose a novel continual self-supervised learning (CSSL) framework for
> simultaneously learning diverse features from multi-window-obtained chest
> computed tomography (CT) images and ensuring data privacy. Achieving a robust
> and highly generalizable model in medical image diagnosis is challenging,
> mainly because of issues, such as the scarcity of large-scale, accurately
> annotated datasets and domain shifts inherent to dynamic healthcare
> environments. Specifically, in chest CT, these domain shifts often arise from
> differences in window settings, which are optimized for distinct clinical
> purposes. Previous CSSL frameworks often mitigated domain shift by reusing past
> data, a typically impractical approach owing to privacy constraints. Our
> approach addresses these challenges by effectively capturing the relationship
> between previously learned knowledge and new information across different
> training stages through continual pretraining on unlabeled images.
> Specifically, by incorporating a latent replay-based mechanism into CSSL, our
> method mitigates catastrophic forgetting due to domain shifts during continual
> pretraining while ensuring data privacy. Additionally, we introduce a feature
> distillation technique that integrates Wasserstein distance-based knowledge
> distillation (WKD) and batch-knowledge ensemble (BKE), enhancing the ability of
> the model to learn meaningful, domain-shift-robust representations. Finally, we
> validate our approach using chest CT images obtained across two different
> window settings, demonstrating superior performance compared with other
> approaches.

