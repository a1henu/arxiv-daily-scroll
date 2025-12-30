---
layout: default
title: Theoretical Foundations of Scaling Law in Familial Models
---

# Theoretical Foundations of Scaling Law in Familial Models
**arXiv**：[2512.23407v1](https://arxiv.org/abs/2512.23407) · [PDF](https://arxiv.org/pdf/2512.23407.pdf)  
**作者**：Huan Song, Qingfei Zhao, Ting Long, Shuyu Tian, Hongjun An, Jiawei Shao, Chi Zhang, Xuelong Li  

**一句话要点**：提出基于粒度变量的缩放定律，以支持异构设备-边缘-云层次中的家族模型范式。

**关键词**：缩放定律, 家族模型, 异构计算, 动态架构, IsoFLOP实验

## 3 点简述
- 核心问题：传统缩放定律忽略家族模型，无法量化其动态架构对性能的影响。
- 方法要点：引入粒度作为缩放变量，构建统一函数形式，并通过IsoFLOP实验设计参数化。
- 实验或效果：发现粒度惩罚遵循乘性幂律，验证了“一次训练，多次部署”的可行性。

## 摘要（原文）

> Neural scaling laws have become foundational for optimizing large language model (LLM) training, yet they typically assume a single dense model output. This limitation effectively overlooks "Familial models, a transformative paradigm essential for realizing ubiquitous intelligence across heterogeneous device-edge-cloud hierarchies. Transcending static architectures, familial models integrate early exits with relay-style inference to spawn G deployable sub-models from a single shared backbone. In this work, we theoretically and empirically extend the scaling law to capture this "one-run, many-models" paradigm by introducing Granularity (G) as a fundamental scaling variable alongside model size (N) and training tokens (D). To rigorously quantify this relationship, we propose a unified functional form L(N, D, G) and parameterize it using large-scale empirical runs. Specifically, we employ a rigorous IsoFLOP experimental design to strictly isolate architectural impact from computational scale. Across fixed budgets, we systematically sweep model sizes (N) and granularities (G) while dynamically adjusting tokens (D). This approach effectively decouples the marginal cost of granularity from the benefits of scale, ensuring high-fidelity parameterization of our unified scaling law. Our results reveal that the granularity penalty follows a multiplicative power law with an extremely small exponent. Theoretically, this bridges fixed-compute training with dynamic architectures. Practically, it validates the "train once, deploy many" paradigm, demonstrating that deployment flexibility is achievable without compromising the compute-optimality of dense baselines.

