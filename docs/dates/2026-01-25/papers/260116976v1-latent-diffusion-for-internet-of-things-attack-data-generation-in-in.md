---
layout: default
title: Latent Diffusion for Internet of Things Attack Data Generation in Intrusion Detection
---

# Latent Diffusion for Internet of Things Attack Data Generation in Intrusion Detection
**arXiv**：[2601.16976v1](https://arxiv.org/abs/2601.16976) · [PDF](https://arxiv.org/pdf/2601.16976.pdf)  
**作者**：Estela Sánchez-Carballo, Francisco M. Melgarejo-Meseguer, José Luis Rojo-Álvarez  

**一句话要点**：提出潜在扩散模型以解决物联网入侵检测中攻击数据类别不平衡问题

**关键词**：物联网入侵检测, 潜在扩散模型, 数据增强, 类别不平衡, 攻击数据生成

## 3 点简述
- 物联网入侵检测系统面临攻击与良性流量类别不平衡，影响机器学习性能。
- 使用潜在扩散模型生成攻击数据，平衡训练集，提升样本保真度、多样性和计算效率。
- 实验在DDoS、Mirai和中间人攻击上验证，F1分数达0.99，采样时间减少约25%。

## 摘要（原文）

> Intrusion Detection Systems (IDSs) are a key component for protecting Internet of Things (IoT) environments. However, in Machine Learning-based (ML-based) IDSs, performance is often degraded by the strong class imbalance between benign and attack traffic. Although data augmentation has been widely explored to mitigate this issue, existing approaches typically rely on simple oversampling techniques or generative models that struggle to simultaneously achieve high sample fidelity, diversity, and computational efficiency. To address these limitations, we propose the use of a Latent Diffusion Model (LDM) for attack data augmentation in IoT intrusion detection and provide a comprehensive comparison against state-of-the-art baselines. Experiments were conducted on three representative IoT attack types, specifically Distributed Denial-of-Service (DDoS), Mirai, and Man-in-the-Middle, evaluating both downstream IDS performance and intrinsic generative quality using distributional, dependency-based, and diversity metrics. Results show that balancing the training data with LDM-generated samples substantially improves IDS performance, achieving F1-scores of up to 0.99 for DDoS and Mirai attacks and consistently outperforming competing methods. Additionally, quantitative and qualitative analyses demonstrate that LDMs effectively preserve feature dependencies while generating diverse samples and reduce sampling time by approximately 25\% compared to diffusion models operating directly in data space. These findings highlight latent diffusion as an effective and scalable solution for synthetic IoT attack data generation, substantially mitigating the impact of class imbalance in ML-based IDSs for IoT scenarios.

