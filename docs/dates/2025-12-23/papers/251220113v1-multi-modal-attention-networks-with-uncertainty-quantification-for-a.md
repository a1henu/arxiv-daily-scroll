---
layout: default
title: Multi Modal Attention Networks with Uncertainty Quantification for Automated Concrete Bridge Deck Delamination Detection
---

# Multi Modal Attention Networks with Uncertainty Quantification for Automated Concrete Bridge Deck Delamination Detection
**arXiv**：[2512.20113v1](https://arxiv.org/abs/2512.20113) · [PDF](https://arxiv.org/pdf/2512.20113.pdf)  
**作者**：Alireza Moayedikia, Sattar Dorafshan  

**一句话要点**：提出多模态注意力网络融合雷达与热成像，用于桥梁板脱层检测，并量化不确定性。

**关键词**：多模态融合, 注意力机制, 不确定性量化, 桥梁检测, 脱层检测, 实时检查

## 3 点简述
- 核心问题：单模态检测方法在桥梁板脱层检测中受限于互补约束，如雷达对湿度和浅层缺陷敏感，热成像依赖天气且深度有限。
- 方法要点：设计多模态注意力网络，结合雷达时间注意力和热成像空间注意力，通过可学习嵌入进行跨模态融合，并集成蒙特卡洛dropout和方差估计量化不确定性。
- 实验或效果：在五个桥梁数据集上，该方法在平衡至中度不平衡数据中显著优于基线，但极端类别不平衡下注意力机制易受多数类崩溃影响。

## 摘要（原文）

> Deteriorating civil infrastructure requires automated inspection techniques overcoming limitations of visual assessment. While Ground Penetrating Radar and Infrared Thermography enable subsurface defect detection, single modal approaches face complementary constraints radar struggles with moisture and shallow defects, while thermography exhibits weather dependency and limited depth. This paper presents a multi modal attention network fusing radar temporal patterns with thermal spatial signatures for bridge deck delamination detection. Our architecture introduces temporal attention for radar processing, spatial attention for thermal features, and cross modal fusion with learnable embeddings discovering complementary defect patterns invisible to individual sensors. We incorporate uncertainty quantification through Monte Carlo dropout and learned variance estimation, decomposing uncertainty into epistemic and aleatoric components for safety critical decisions. Experiments on five bridge datasets reveal that on balanced to moderately imbalanced data, our approach substantially outperforms baselines in accuracy and AUC representing meaningful improvements over single modal and concatenation based fusion. Ablation studies demonstrate cross modal attention provides critical gains beyond within modality attention, while multi head mechanisms achieve improved calibration. Uncertainty quantification reduces calibration error, enabling selective prediction by rejecting uncertain cases. However, under extreme class imbalance, attention mechanisms show vulnerability to majority class collapse. These findings provide actionable guidance: attention based architecture performs well across typical scenarios, while extreme imbalance requires specialized techniques. Our system maintains deployment efficiency, enabling real time inspection with characterized capabilities and limitations.

