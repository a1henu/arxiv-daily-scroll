---
layout: default
title: DentalGPT: Incentivizing Multimodal Complex Reasoning in Dentistry
---

# DentalGPT: Incentivizing Multimodal Complex Reasoning in Dentistry
**arXiv**：[2512.11558v1](https://arxiv.org/abs/2512.11558) · [PDF](https://arxiv.org/pdf/2512.11558.pdf)  
**作者**：Zhenyang Cai, Jiaming Zhang, Junjie Zhao, Ziyi Zeng, Yanchao Li, Jingyi Liang, Junying Chen, Yunjin Yang, Jiajun You, Shuzhi Deng, Tongfei Wang, Wanting Chen, Chunxiu Hao, Ruiqi Xie, Zhenwei Wen, Xiangyi Feng, Zou Ting, Jin Zou Lin, Jianquan Li, Guangjun Yu, Liangyi Chen, Junwen Wang, Shan Jiang, Benyou Wang  

**一句话要点**：提出DentalGPT以解决牙科多模态数据精细视觉理解与复杂推理不足的问题

**关键词**：牙科多模态大语言模型, 领域知识注入, 强化学习, 牙科视觉问答, 疾病分类, 多模态数据集

## 3 点简述
- 当前多模态大语言模型在牙科领域难以捕捉细粒度视觉细节且推理能力不足
- 通过高质量领域知识注入和强化学习构建专用牙科多模态大语言模型
- 在牙科基准测试中表现优异，优于许多先进模型，参数仅7B

## 摘要（原文）

> Reliable interpretation of multimodal data in dentistry is essential for automated oral healthcare, yet current multimodal large language models (MLLMs) struggle to capture fine-grained dental visual details and lack sufficient reasoning ability for precise diagnosis. To address these limitations, we present DentalGPT, a specialized dental MLLM developed through high-quality domain knowledge injection and reinforcement learning. Specifically, the largest annotated multimodal dataset for dentistry to date was constructed by aggregating over 120k dental images paired with detailed descriptions that highlight diagnostically relevant visual features, making it the multimodal dataset with the most extensive collection of dental images to date. Training on this dataset significantly enhances the MLLM's visual understanding of dental conditions, while the subsequent reinforcement learning stage further strengthens its capability for multimodal complex reasoning. Comprehensive evaluations on intraoral and panoramic benchmarks, along with dental subsets of medical VQA benchmarks, show that DentalGPT achieves superior performance in disease classification and dental VQA tasks, outperforming many state-of-the-art MLLMs despite having only 7B parameters. These results demonstrate that high-quality dental data combined with staged adaptation provides an effective pathway for building capable and domain-specialized dental MLLMs.

