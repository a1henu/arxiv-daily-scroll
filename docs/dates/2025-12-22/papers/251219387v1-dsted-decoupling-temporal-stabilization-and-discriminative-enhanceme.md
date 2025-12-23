---
layout: default
title: DSTED: Decoupling Temporal Stabilization and Discriminative Enhancement for Surgical Workflow Recognition
---

# DSTED: Decoupling Temporal Stabilization and Discriminative Enhancement for Surgical Workflow Recognition
**arXiv**：[2512.19387v1](https://arxiv.org/abs/2512.19387) · [PDF](https://arxiv.org/pdf/2512.19387.pdf)  
**作者**：Yueyao Chen, Kai-Ni Wang, Dario Tayupo, Arnaud Huaulm'e, Krystel Nyangoh Timoh, Pierre Jannin, Qi Dou  

**一句话要点**：提出DSTED框架，通过解耦时间稳定性和判别性增强，解决手术工作流识别中的预测抖动和模糊阶段区分难题。

**关键词**：手术工作流识别, 时间稳定性, 判别性增强, 双路径框架, 不确定性建模, 计算机辅助干预

## 3 点简述
- 核心问题：手术工作流识别存在连续帧预测抖动和模糊阶段区分差的问题。
- 方法要点：采用双路径设计，包括可靠记忆传播和不确定性感知原型检索，动态平衡时间一致性与样本增强。
- 实验或效果：在AutoLaparo-hysterectomy数据集上达到84.36%准确率，显著减少抖动并提升挑战性阶段过渡性能。

## 摘要（原文）

> Purpose: Surgical workflow recognition enables context-aware assistance and skill assessment in computer-assisted interventions. Despite recent advances, current methods suffer from two critical challenges: prediction jitter across consecutive frames and poor discrimination of ambiguous phases. This paper aims to develop a stable framework by selectively propagating reliable historical information and explicitly modeling uncertainty for hard sample enhancement.
>   Methods: We propose a dual-pathway framework DSTED with Reliable Memory Propagation (RMP) and Uncertainty-Aware Prototype Retrieval (UPR). RMP maintains temporal coherence by filtering and fusing high-confidence historical features through multi-criteria reliability assessment. UPR constructs learnable class-specific prototypes from high-uncertainty samples and performs adaptive prototype matching to refine ambiguous frame representations. Finally, a confidence-driven gate dynamically balances both pathways based on prediction certainty.
>   Results: Our method achieves state-of-the-art performance on AutoLaparo-hysterectomy with 84.36% accuracy and 65.51% F1-score, surpassing the second-best method by 3.51% and 4.88% respectively. Ablations reveal complementary gains from RMP (2.19%) and UPR (1.93%), with synergistic effects when combined. Extensive analysis confirms substantial reduction in temporal jitter and marked improvement on challenging phase transitions.
>   Conclusion: Our dual-pathway design introduces a novel paradigm for stable workflow recognition, demonstrating that decoupling the modeling of temporal consistency and phase ambiguity yields superior performance and clinical applicability.

