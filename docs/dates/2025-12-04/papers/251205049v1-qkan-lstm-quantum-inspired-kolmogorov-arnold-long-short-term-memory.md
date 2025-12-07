---
layout: default
title: QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory
---

# QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory
**arXiv**：[2512.05049v1](https://arxiv.org/abs/2512.05049) · [PDF](https://arxiv.org/pdf/2512.05049.pdf)  
**作者**：Yu-Chao Hsu, Jiun-Cheng Jiang, Chun-Hua Lin, Kuo-Chung Peng, Nan-Yow Chen, Samuel Yen-Chi Chen, En-Jui Kuo, Hsi-Sheng Goan  

**一句话要点**：提出QKAN-LSTM以解决LSTM参数冗余和非线性表达能力不足的问题，应用于序列建模任务。

**关键词**：量子启发神经网络, 长短期记忆网络, 序列建模, 参数优化, 非线性激活函数, 城市电信预测

## 3 点简述
- 传统LSTM存在高参数冗余和有限非线性表达能力的问题。
- 集成DARUAN模块作为量子变分激活函数，增强频率适应性和谱表示，无需多量子比特纠缠。
- 在三个数据集上实验显示，参数减少79%且预测准确性和泛化能力优于经典LSTM。

## 摘要（原文）

> Long short-term memory (LSTM) models are a particular type of recurrent neural networks (RNNs) that are central to sequential modeling tasks in domains such as urban telecommunication forecasting, where temporal correlations and nonlinear dependencies dominate. However, conventional LSTMs suffer from high parameter redundancy and limited nonlinear expressivity. In this work, we propose the Quantum-inspired Kolmogorov-Arnold Long Short-Term Memory (QKAN-LSTM), which integrates Data Re-Uploading Activation (DARUAN) modules into the gating structure of LSTMs. Each DARUAN acts as a quantum variational activation function (QVAF), enhancing frequency adaptability and enabling an exponentially enriched spectral representation without multi-qubit entanglement. The resulting architecture preserves quantum-level expressivity while remaining fully executable on classical hardware. Empirical evaluations on three datasets, Damped Simple Harmonic Motion, Bessel Function, and Urban Telecommunication, demonstrate that QKAN-LSTM achieves superior predictive accuracy and generalization with a 79% reduction in trainable parameters compared to classical LSTMs. We extend the framework to the Jiang-Huang-Chen-Goan Network (JHCG Net), which generalizes KAN to encoder-decoder structures, and then further use QKAN to realize the latent KAN, thereby creating a Hybrid QKAN (HQKAN) for hierarchical representation learning. The proposed HQKAN-LSTM thus provides a scalable and interpretable pathway toward quantum-inspired sequential modeling in real-world data environments.

