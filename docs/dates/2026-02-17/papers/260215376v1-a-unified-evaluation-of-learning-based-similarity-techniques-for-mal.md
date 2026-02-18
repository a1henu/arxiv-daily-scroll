---
layout: default
title: A Unified Evaluation of Learning-Based Similarity Techniques for Malware Detection
---

# A Unified Evaluation of Learning-Based Similarity Techniques for Malware Detection
**arXiv**：[2602.15376v1](https://arxiv.org/abs/2602.15376) · [PDF](https://arxiv.org/pdf/2602.15376.pdf)  
**作者**：Udbhav Prasad, Aniesh Chawla  

**一句话要点**：系统评估学习型相似性技术，揭示互补组合在恶意软件检测中的必要性

**关键词**：恶意软件检测, 相似性技术, 机器学习评估, 安全应用, 统一框架

## 3 点简述
- 核心问题：传统哈希方法因单比特变化导致完全不同的哈希，不适用于恶意软件检测等需要近似匹配的场景
- 方法要点：在统一框架下比较基于机器学习的分类和相似性方法，使用公开数据集和行业标准指标
- 实验或效果：结果显示无单一方法在所有维度表现最佳，需结合互补技术以提升检测效果

## 摘要（原文）

> Cryptographic digests (e.g., MD5, SHA-256) are designed to provide exact identity. Any single-bit change in the input produces a completely different hash, which is ideal for integrity verification but limits their usefulness in many real-world tasks like threat hunting, malware analysis and digital forensics, where adversaries routinely introduce minor transformations. Similarity-based techniques address this limitation by enabling approximate matching, allowing related byte sequences to produce measurably similar fingerprints. Modern enterprises manage tens of thousands of endpoints with billions of files, making the effectiveness and scalability of the proposed techniques more important than ever in security applications. Security researchers have proposed a range of approaches, including similarity digests and locality-sensitive hashes (e.g., ssdeep, sdhash, TLSH), as well as more recent machine-learning-based methods that generate embeddings from file features. However, these techniques have largely been evaluated in isolation, using disparate datasets and evaluation criteria. This paper presents a systematic comparison of learning-based classification and similarity methods using large, publicly available datasets. We evaluate each method under a unified experimental framework with industry-accepted metrics. To our knowledge, this is the first reproducible study to benchmark these diverse learning-based similarity techniques side by side for real-world security workloads. Our results show that no single approach performs well across all dimensions; instead, each exhibits distinct trade-offs, indicating that effective malware analysis and threat-hunting platforms must combine complementary classification and similarity techniques rather than rely on a single method.

