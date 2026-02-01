---
layout: default
title: Accurate Network Traffic Matrix Prediction via LEAD: an LLM-Enhanced Adapter-Based Conditional Diffusion Model
---

# Accurate Network Traffic Matrix Prediction via LEAD: an LLM-Enhanced Adapter-Based Conditional Diffusion Model
**arXiv**：[2601.21437v1](https://arxiv.org/abs/2601.21437) · [PDF](https://arxiv.org/pdf/2601.21437.pdf)  
**作者**：Yu Sun, Yaqiong Liu, Nan Cheng, Jiayuan Li, Zihan Jia, Xialin Du, Mugen Peng  

**一句话要点**：提出LEAD模型以解决网络流量矩阵预测中的不确定性和非线性挑战

**关键词**：网络流量预测, 扩散模型, LLM增强, 条件生成, 图像化表示, 不确定性建模

## 3 点简述
- 核心问题：网络流量矩阵预测因随机性、非线性和突发性而困难，现有模型易过平滑且不确定性感知有限
- 方法要点：采用流量转图像范式，结合冻结LLM与可训练适配器，设计双条件策略引导扩散模型生成流量矩阵
- 实验或效果：在Abilene和GEANT数据集上，LEAD显著降低RMSE，如Abilene数据集RMSE减少45.2%，预测误差随步长增加变化小

## 摘要（原文）

> Driven by the evolution toward 6G and AI-native edge intelligence, network operations increasingly require predictive and risk-aware adaptation under stringent computation and latency constraints. Network Traffic Matrix (TM), which characterizes flow volumes between nodes, is a fundamental signal for proactive traffic engineering. However, accurate TM forecasting remains challenging due to the stochastic, non-linear, and bursty nature of network dynamics. Existing discriminative models often suffer from over-smoothing and provide limited uncertainty awareness, leading to poor fidelity under extreme bursts. To address these limitations, we propose LEAD, a Large Language Model (LLM)-Enhanced Adapter-based conditional Diffusion model. First, LEAD adopts a "Traffic-to-Image" paradigm to transform traffic matrices into RGB images, enabling global dependency modeling via vision backbones. Then, we design a "Frozen LLM with Trainable Adapter" model, which efficiently captures temporal semantics with limited computational cost. Moreover, we propose a Dual-Conditioning Strategy to precisely guide a diffusion model to generate complex, dynamic network traffic matrices. Experiments on the Abilene and GEANT datasets demonstrate that LEAD outperforms all baselines. On the Abilene dataset, LEAD attains a remarkable 45.2% reduction in RMSE against the best baseline, with the error margin rising only marginally from 0.1098 at one-step to 0.1134 at 20-step predictions. Meanwhile, on the GEANT dataset, LEAD achieves a 0.0258 RMSE at 20-step prediction horizon which is 27.3% lower than the best baseline.

