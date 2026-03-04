---
layout: default
title: Integrating Homomorphic Encryption and Synthetic Data in FL for Privacy and Learning Quality
---

# Integrating Homomorphic Encryption and Synthetic Data in FL for Privacy and Learning Quality
**arXiv**：[2603.02969v1](https://arxiv.org/abs/2603.02969) · [PDF](https://arxiv.org/pdf/2603.02969.pdf)  
**作者**：Yenan Wang, Carla Fabiana Chiasserini, Elad Michael Schiller  

**一句话要点**：提出交替联邦学习以在隐私保护中提升学习质量并降低计算成本

**关键词**：联邦学习, 同态加密, 合成数据, 隐私保护, 模型准确率, 计算成本

## 3 点简述
- 联邦学习面临隐私保护与学习质量的双重挑战，尤其在使用同态加密时资源消耗高
- 通过交替使用真实数据与合成数据进行本地训练，并结合加密与明文参数传输，增强隐私与学习效果
- 实验显示，该方法能抵御数据泄漏攻击，提升模型准确率13.4%，并降低同态加密成本达48%

## 摘要（原文）

> Federated learning (FL) enables collaborative training of machine learning models without sharing sensitive client data, making it a cornerstone for privacy-critical applications. However, FL faces the dual challenge of ensuring learning quality and robust privacy protection while keeping resource consumption low, particularly when using computationally expensive techniques such as homomorphic encryption (HE). In this work, we enhance an FL process that preserves privacy using HE by integrating it with synthetic data generation and an interleaving strategy. Specifically, our solution, named Alternating Federated Learning (Alt-FL), consists of alternating between local training with authentic data (authentic rounds) and local training with synthetic data (synthetic rounds) and transferring the encrypted and plaintext model parameters on authentic and synthetic rounds (resp.). Our approach improves learning quality (e.g., model accuracy) through datasets enhanced with synthetic data, preserves client data privacy via HE, and keeps manageable encryption and decryption costs through our interleaving strategy. We evaluate our solution against data leakage attacks, such as the DLG attack, demonstrating robust privacy protection. Also, Alt-FL provides 13.4% higher model accuracy and decreases HE-related costs by up to 48% with respect to Selective HE.

