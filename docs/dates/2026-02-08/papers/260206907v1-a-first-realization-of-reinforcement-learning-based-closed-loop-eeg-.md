---
layout: default
title: A first realization of reinforcement learning-based closed-loop EEG-TMS
---

# A first realization of reinforcement learning-based closed-loop EEG-TMS
**arXiv**：[2602.06907v1](https://arxiv.org/abs/2602.06907) · [PDF](https://arxiv.org/pdf/2602.06907.pdf)  
**作者**：Dania Humaidan, Jiahua Xu, Jing Chen, Christoph Zrenner, David Emanuel Vetter, Laura Marzetti, Paolo Belardinelli, Timo Roine, Risto J. Ilmoniemi, Gian Luca Romani, Ulf Zieman  

**一句话要点**：提出基于强化学习的闭环EEG-TMS系统，实现个体化脑刺激以优化神经可塑性。

**关键词**：闭环脑刺激, 强化学习, EEG-TMS, 神经可塑性, 个体化治疗

## 3 点简述
- 传统TMS治疗忽视个体差异，需用户定义目标相位，限制了精准性。
- 采用强化学习算法，实时识别与高/低皮质脊髓兴奋性相关的mu节律相位。
- 实验显示，强化学习能有效识别相位，重复刺激导致功能连接性长期变化。

## 摘要（原文）

> Background: Transcranial magnetic stimulation (TMS) is a powerful tool to investigate neurophysiology of the human brain and treat brain disorders. Traditionally, therapeutic TMS has been applied in a one-size-fits-all approach, disregarding inter- and intra-individual differences. Brain state-dependent EEG-TMS, such as coupling TMS with a pre-specified phase of the sensorimotor mu-rhythm, enables the induction of differential neuroplastic effects depending on the targeted phase. But this approach is still user-dependent as it requires defining an a-priori target phase. Objectives: To present a first realization of a machine-learning-based, closed-loop real-time EEG-TMS setup to identify user-independently the individual mu-rhythm phase associated with high- vs. low-corticospinal excitability states. Methods: We applied EEG-TMS to 25 participants targeting the supplementary motor area-primary motor cortex network and used a reinforcement learning algorithm to identify the mu-rhythm phase associated with high- vs. low corticospinal excitability. We employed linear mixed effects models and Bayesian analysis to determine effects of reinforced learning on corticospinal excitability indexed by motor evoked potential amplitude, and functional connectivity indexed by the imaginary part of resting-state EEG coherence. Results: Reinforcement learning effectively identified the mu-rhythm phase associated with high- vs. low-excitability states, and their repetitive stimulation resulted in long-term increases vs. decreases in functional connectivity in the stimulated sensorimotor network. Conclusions: We demonstrated for the first time the feasibility of closed-loop EEG-TMS in humans, a critical step towards individualized treatment of brain disorders.

