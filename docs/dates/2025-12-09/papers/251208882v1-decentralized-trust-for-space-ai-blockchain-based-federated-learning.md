---
layout: default
title: Decentralized Trust for Space AI: Blockchain-Based Federated Learning Across Multi-Vendor LEO Satellite Networks
---

# Decentralized Trust for Space AI: Blockchain-Based Federated Learning Across Multi-Vendor LEO Satellite Networks
**arXiv**：[2512.08882v1](https://arxiv.org/abs/2512.08882) · [PDF](https://arxiv.org/pdf/2512.08882.pdf)  
**作者**：Mohamed Elmahallawy, Asma Jodeiri Akbarfam  

**一句话要点**：提出OrbitChain框架，通过区块链增强多供应商LEO卫星网络中的联邦学习信任与效率

**关键词**：联邦学习, 区块链, 低地球轨道卫星, 信任机制, 多供应商协作, 高空平台

## 3 点简述
- 核心问题：联邦卫星学习面临间歇连接导致收敛慢，以及跨星座更新可能被篡改的信任挑战
- 方法要点：利用高空平台卸载共识，确保模型更新可审计，防止恶意贡献影响聚合
- 实验或效果：仿真显示降低开销，提升隐私安全与模型精度，收敛时间减少达30小时

## 摘要（原文）

> The rise of space AI is reshaping government and industry through applications such as disaster detection, border surveillance, and climate monitoring, powered by massive data from commercial and governmental low Earth orbit (LEO) satellites. Federated satellite learning (FSL) enables joint model training without sharing raw data, but suffers from slow convergence due to intermittent connectivity and introduces critical trust challenges--where biased or falsified updates can arise across satellite constellations, including those injected through cyberattacks on inter-satellite or satellite-ground communication links. We propose OrbitChain, a blockchain-backed framework that empowers trustworthy multi-vendor collaboration in LEO networks. OrbitChain (i) offloads consensus to high-altitude platforms (HAPs) with greater computational capacity, (ii) ensures transparent, auditable provenance of model updates from different orbits owned by different vendors, and (iii) prevents manipulated or incomplete contributions from affecting global FSL model aggregation. Extensive simulations show that OrbitChain reduces computational and communication overhead while improving privacy, security, and global model accuracy. Its permissioned proof-of-authority ledger finalizes over 1000 blocks with sub-second latency (0.16,s, 0.26,s, 0.35,s for 1-of-5, 3-of-5, and 5-of-5 quorums). Moreover, OrbitChain reduces convergence time by up to 30 hours on real satellite datasets compared to single-vendor, demonstrating its effectiveness for real-time, multi-vendor learning. Our code is available at https://github.com/wsu-cyber-security-lab-ai/OrbitChain.git

