---
layout: default
title: Hold-One-Shot-Out (HOSO) for Validation-Free Few-Shot CLIP Adapters
---

# Hold-One-Shot-Out (HOSO) for Validation-Free Few-Shot CLIP Adapters
**arXiv**：[2603.04341v1](https://arxiv.org/abs/2603.04341) · [PDF](https://arxiv.org/pdf/2603.04341.pdf)  
**作者**：Chris Vorster, Mayug Maniparambil, Noel E. O'Connor, Noel Murphy, Derek Molloy  

**一句话要点**：提出Hold-One-Shot-Out方法以解决CLIP适配器中无需验证集的少样本学习问题

**关键词**：CLIP适配器, 少样本学习, 验证自由, 混合比学习, Hold-One-Shot-Out

## 3 点简述
- 核心问题：现有CLIP适配器需验证集或测试集调优混合比，违反严格少样本设定
- 方法要点：使用单样本留出机制学习混合比，适配器在剩余少样本上训练
- 实验或效果：在11个数据集上平均提升4个百分点以上，优于基线甚至最优测试集调优

## 摘要（原文）

> In many CLIP adaptation methods, a blending ratio hyperparameter controls the trade-off between general pretrained CLIP knowledge and the limited, dataset-specific supervision from the few-shot cases. Most few-shot CLIP adaptation techniques report results by ablation of the blending ratio on the test set or require additional validation sets to select the blending ratio per dataset, and thus are not strictly few-shot. We present a simple, validation-free method for learning the blending ratio in CLIP adaptation. Hold-One-Shot-Out (HOSO) presents a novel approach for CLIP-Adapter-style methods to compete in the newly established validation-free setting. CLIP-Adapter with HOSO (HOSO-Adapter) learns the blending ratio using a one-shot, hold-out set, while the adapter trains on the remaining few-shot support examples. Under the validation-free few-shot protocol, HOSO-Adapter outperforms the CLIP-Adapter baseline by more than 4 percentage points on average across 11 standard few-shot datasets. Interestingly, in the 8- and 16-shot settings, HOSO-Adapter outperforms CLIP-Adapter even with the optimal blending ratio selected on the test set. Ablation studies validate the use of a one-shot hold-out mechanism, decoupled training, and improvements over the naively learnt blending ratio baseline. Code is released here: https://github.com/chris-vorster/HOSO-Adapter

