---
layout: default
title: PrivTune: Efficient and Privacy-Preserving Fine-Tuning of Large Language Models via Device-Cloud Collaboration
---

# PrivTune: Efficient and Privacy-Preserving Fine-Tuning of Large Language Models via Device-Cloud Collaboration
**arXiv**：[2512.08809v1](https://arxiv.org/abs/2512.08809) · [PDF](https://arxiv.org/pdf/2512.08809.pdf)  
**作者**：Yi Liu, Weixiang Han, Chengjun Cai, Xingliang Yuan, Cong Wang  

**一句话要点**：提出PrivTune框架，通过设备-云协作实现大语言模型高效隐私保护微调

**关键词**：隐私保护微调, 设备-云协作, Split Learning, 令牌噪声注入, 大语言模型安全

## 3 点简述
- 核心问题：现有差分隐私方法在设备-云协作中难以平衡隐私与效用，易导致敏感数据泄露或性能下降
- 方法要点：基于Split Learning，向底层模型令牌表示注入优化噪声，使令牌类似间接邻居，并调整噪声分布参数以最小化失真
- 实验或效果：在五个数据集上对抗六种攻击，PrivTune将攻击成功率降至10%，效用性能仅下降3.33%，优于基线方法

## 摘要（原文）

> With the rise of large language models, service providers offer language models as a service, enabling users to fine-tune customized models via uploaded private datasets. However, this raises concerns about sensitive data leakage. Prior methods, relying on differential privacy within device-cloud collaboration frameworks, struggle to balance privacy and utility, exposing users to inference attacks or degrading fine-tuning performance. To address this, we propose PrivTune, an efficient and privacy-preserving fine-tuning framework via Split Learning (SL). The key idea of PrivTune is to inject crafted noise into token representations from the SL bottom model, making each token resemble the $n$-hop indirect neighbors. PrivTune formulates this as an optimization problem to compute the optimal noise vector, aligning with defense-utility goals. On this basis, it then adjusts the parameters (i.e., mean) of the $d_χ$-Privacy noise distribution to align with the optimization direction and scales the noise according to token importance to minimize distortion. Experiments on five datasets (covering both classification and generation tasks) against three embedding inversion and three attribute inference attacks show that, using RoBERTa on the Stanford Sentiment Treebank dataset, PrivTune reduces the attack success rate to 10% with only a 3.33% drop in utility performance, outperforming state-of-the-art baselines.

