---
layout: default
title: PhyGHT: Physics-Guided HyperGraph Transformer for Signal Purification at the HL-LHC
---

# PhyGHT: Physics-Guided HyperGraph Transformer for Signal Purification at the HL-LHC
**arXiv**：[2602.20475v1](https://arxiv.org/abs/2602.20475) · [PDF](https://arxiv.org/pdf/2602.20475.pdf)  
**作者**：Mohammed Rakib, Luke Vaughan, Shivang Patel, Flera Rizatdinova, Alexander Khanov, Atriya Sen  

**一句话要点**：提出PhyGHT以解决HL-LHC极端堆积噪声下的信号净化问题

**关键词**：信号净化, 超图变换器, 堆积噪声抑制, 物理引导学习, 高能物理重建

## 3 点简述
- HL-LHC中约200次同时堆积碰撞导致信号被严重噪声覆盖，影响物理观测重建
- 结合距离感知局部图注意力和全局自注意力，并引入可解释的堆积抑制门过滤软噪声
- 在模拟数据集上优于ATLAS和CMS基线，准确预测能量和质量校正因子

## 摘要（原文）

> The High-Luminosity Large Hadron Collider (HL-LHC) at CERN will produce unprecedented datasets capable of revealing fundamental properties of the universe. However, realizing its discovery potential faces a significant challenge: extracting small signal fractions from overwhelming backgrounds dominated by approximately 200 simultaneous pileup collisions. This extreme noise severely distorts the physical observables required for accurate reconstruction. To address this, we introduce the Physics-Guided Hypergraph Transformer (PhyGHT), a hybrid architecture that combines distance-aware local graph attention with global self-attention to mirror the physical topology of particle showers formed in proton-proton collisions. Crucially, we integrate a Pileup Suppression Gate (PSG), an interpretable, physics-constrained mechanism that explicitly learns to filter soft noise prior to hypergraph aggregation. To validate our approach, we release a novel simulated dataset of top-quark pair production to model extreme pileup conditions. PhyGHT outperforms state-of-the-art baselines from the ATLAS and CMS experiments in predicting the signal's energy and mass correction factors. By accurately reconstructing the top quark's invariant mass, we demonstrate how machine learning innovation and interdisciplinary collaboration can directly advance scientific discovery at the frontiers of experimental physics and enhance the HL-LHC's discovery potential. The dataset and code are available at https://github.com/rAIson-Lab/PhyGHT

