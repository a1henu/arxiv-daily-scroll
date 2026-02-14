---
layout: default
title: MiniCPM-SALA: Hybridizing Sparse and Linear Attention for Efficient Long-Context Modeling
---

# MiniCPM-SALA: Hybridizing Sparse and Linear Attention for Efficient Long-Context Modeling
**arXiv**：[2602.11761v1](https://arxiv.org/abs/2602.11761) · [PDF](https://arxiv.org/pdf/2602.11761.pdf)  
**作者**：MiniCPM Team, Wenhao An, Yingfa Chen, Yewei Fang, Jiayi Li, Xin Li, Yaohui Li, Yishan Li, Yuxuan Li, Biyuan Lin, Chuan Liu, Hezi Liu, Siyuan Liu, Hongya Lyu, Yinxu Pan, Shixin Ren, Xingyu Shen, Zhou Su, Haojun Sun, Yangang Sun, Zhen Leng Thai, Xin Tian, Rui Wang, Xiaorong Wang, Yudong Wang, Bo Wu, Xiaoyue Xu, Dong Xu, Shuaikang Xue, Jiawei Yang, Bowen Zhang, Jinqian Zhang, Letian Zhang, Shengnan Zhang, Xinyu Zhang, Xinyuan Zhang, Zhu Zhang, Hengyu Zhao, Jiacheng Zhao, Jie Zhou, Zihan Zhou, Shuo Wang, Chaojun Xiao, Xu Han, Zhiyuan Liu, Maosong Sun  

**一句话要点**：提出MiniCPM-SALA混合稀疏与线性注意力，以高效处理长上下文任务。

**关键词**：长上下文建模, 混合注意力机制, 高效训练框架, 稀疏注意力, 线性注意力, 位置编码

## 3 点简述
- 核心问题：Transformer架构在超长上下文应用中面临高计算和内存成本挑战。
- 方法要点：结合稀疏注意力（InfLLM-V2）和线性注意力（Lightning Attention），采用1:3比例层选择算法和混合位置编码（HyPE）。
- 实验或效果：在单GPU上，256K序列长度推理速度提升3.5倍，支持1M上下文长度，训练成本降低约75%。

## 摘要（原文）

> The evolution of large language models (LLMs) towards applications with ultra-long contexts faces challenges posed by the high computational and memory costs of the Transformer architecture. While existing sparse and linear attention mechanisms attempt to mitigate these issues, they typically involve a trade-off between memory efficiency and model performance. This paper introduces MiniCPM-SALA, a 9B-parameter hybrid architecture that integrates the high-fidelity long-context modeling of sparse attention (InfLLM-V2) with the global efficiency of linear attention (Lightning Attention). By employing a layer selection algorithm to integrate these mechanisms in a 1:3 ratio and utilizing a hybrid positional encoding (HyPE), the model maintains efficiency and performance for long-context tasks. Furthermore, we introduce a cost-effective continual training framework that transforms pre-trained Transformer-based models into hybrid models, which reduces training costs by approximately 75% compared to training from scratch. Extensive experiments show that MiniCPM-SALA maintains general capabilities comparable to full-attention models while offering improved efficiency. On a single NVIDIA A6000D GPU, the model achieves up to 3.5x the inference speed of the full-attention model at the sequence length of 256K tokens and supports context lengths of up to 1M tokens, a scale where traditional full-attention 8B models fail because of memory constraints.

