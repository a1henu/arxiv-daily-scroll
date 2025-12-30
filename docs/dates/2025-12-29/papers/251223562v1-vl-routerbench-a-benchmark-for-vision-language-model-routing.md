---
layout: default
title: VL-RouterBench: A Benchmark for Vision-Language Model Routing
---

# VL-RouterBench: A Benchmark for Vision-Language Model Routing
**arXiv**：[2512.23562v1](https://arxiv.org/abs/2512.23562) · [PDF](https://arxiv.org/pdf/2512.23562.pdf)  
**作者**：Zhehao Huang, Baijiong Lin, Jingyuan Zhang, Jingying Wang, Yuhang Liu, Ning Lu, Tao Li, Xiaolin Huang  

**一句话要点**：提出VL-RouterBench基准以系统评估视觉-语言模型路由能力

**关键词**：视觉-语言模型路由, 基准测试, 多模态系统, 成本效率评估, 开源工具链

## 3 点简述
- 现有视觉-语言模型路由缺乏系统化、可复现的评估基准
- 基于原始推理和评分日志构建质量和成本矩阵，覆盖大规模样本-模型对
- 评估协议联合衡量准确率、成本和吞吐量，并基于归一化指标排名

## 摘要（原文）

> Multi-model routing has evolved from an engineering technique into essential infrastructure, yet existing work lacks a systematic, reproducible benchmark for evaluating vision-language models (VLMs). We present VL-RouterBench to assess the overall capability of VLM routing systems systematically. The benchmark is grounded in raw inference and scoring logs from VLMs and constructs quality and cost matrices over sample-model pairs. In scale, VL-RouterBench covers 14 datasets across 3 task groups, totaling 30,540 samples, and includes 15 open-source models and 2 API models, yielding 519,180 sample-model pairs and a total input-output token volume of 34,494,977. The evaluation protocol jointly measures average accuracy, average cost, and throughput, and builds a ranking score from the harmonic mean of normalized cost and accuracy to enable comparison across router configurations and cost budgets. On this benchmark, we evaluate 10 routing methods and baselines and observe a significant routability gain, while the best current routers still show a clear gap to the ideal Oracle, indicating considerable room for improvement in router architecture through finer visual cues and modeling of textual structure. We will open-source the complete data construction and evaluation toolchain to promote comparability, reproducibility, and practical deployment in multimodal routing research.

