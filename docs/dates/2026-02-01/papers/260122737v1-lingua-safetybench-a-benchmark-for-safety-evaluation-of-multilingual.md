---
layout: default
title: Lingua-SafetyBench: A Benchmark for Safety Evaluation of Multilingual Vision-Language Models
---

# Lingua-SafetyBench: A Benchmark for Safety Evaluation of Multilingual Vision-Language Models
**arXiv**：[2601.22737v1](https://arxiv.org/abs/2601.22737) · [PDF](https://arxiv.org/pdf/2601.22737.pdf)  
**作者**：Enyi Shi, Pengyang Shao, Yanxin Zhang, Chenhang Cui, Jiayi Lyu, Xu Xie, Xiaobo Xia, Fei Shen, Tat-Seng Chua  

**一句话要点**：提出Lingua-SafetyBench基准以评估多语言视觉语言模型在联合多模态输入下的安全性

**关键词**：多语言视觉语言模型, 安全评估基准, 跨模态风险分析, 攻击成功率, 语言资源差异, 图像-文本对

## 3 点简述
- 核心问题：现有基准多为多语言但仅文本或多模态但单语言，缺乏真实跨模态交互覆盖
- 方法要点：构建100,440个有害图像-文本对，分图像主导和文本主导子集以分离风险源
- 实验或效果：评估11个开源VLLM，发现风险不对称性，缩放和升级降低ASR但扩大语言间差距

## 摘要（原文）

> Robust safety of vision-language large models (VLLMs) under joint multilingual and multimodal inputs remains underexplored. Existing benchmarks are typically multilingual but text-only, or multimodal but monolingual. Recent multilingual multimodal red-teaming efforts render harmful prompts into images, yet rely heavily on typography-style visuals and lack semantically grounded image-text pairs, limiting coverage of realistic cross-modal interactions. We introduce Lingua-SafetyBench, a benchmark of 100,440 harmful image-text pairs across 10 languages, explicitly partitioned into image-dominant and text-dominant subsets to disentangle risk sources. Evaluating 11 open-source VLLMs reveals a consistent asymmetry: image-dominant risks yield higher ASR in high-resource languages, while text-dominant risks are more severe in non-high-resource languages. A controlled study on the Qwen series shows that scaling and version upgrades reduce Attack Success Rate (ASR) overall but disproportionately benefit HRLs, widening the gap between HRLs and Non-HRLs under text-dominant risks. This underscores the necessity of language- and modality-aware safety alignment beyond mere scaling.To facilitate reproducibility and future research, we will publicly release our benchmark, model checkpoints, and source code.The code and dataset will be available at https://github.com/zsxr15/Lingua-SafetyBench.Warning: this paper contains examples with unsafe content.

