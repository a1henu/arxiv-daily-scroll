---
layout: default
title: Conv-FinRe: A Conversational and Longitudinal Benchmark for Utility-Grounded Financial Recommendation
---

# Conv-FinRe: A Conversational and Longitudinal Benchmark for Utility-Grounded Financial Recommendation
**arXiv**：[2602.16990v1](https://arxiv.org/abs/2602.16990) · [PDF](https://arxiv.org/pdf/2602.16990.pdf)  
**作者**：Yan Wang, Yi Han, Lingfei Qian, Yueru He, Xueqing Peng, Dongji Feng, Zhuohan Xie, Vincent Jim Zhang, Rosie Guo, Fengran Mo, Jimin Huang, Yankai Chen, Xue Liu, Jian-Yun Nie  

**一句话要点**：提出Conv-FinRe基准以评估金融推荐中LLMs的决策质量与行为模仿的差异

**关键词**：金融推荐基准, 对话式推荐, 长周期评估, 多视角参考, LLM评估, 行为模仿

## 3 点简述
- 核心问题：金融推荐中用户行为可能受市场波动影响，传统基准混淆行为模仿与决策质量
- 方法要点：构建基于真实市场数据和人类决策轨迹的对话式长周期基准，提供多视角参考区分描述性行为与规范性效用
- 实验或效果：评估显示LLMs在理性决策质量与行为对齐间存在张力，数据集和代码已公开

## 摘要（原文）

> Most recommendation benchmarks evaluate how well a model imitates user behavior. In financial advisory, however, observed actions can be noisy or short-sighted under market volatility and may conflict with a user's long-term goals. Treating what users chose as the sole ground truth, therefore, conflates behavioral imitation with decision quality. We introduce Conv-FinRe, a conversational and longitudinal benchmark for stock recommendation that evaluates LLMs beyond behavior matching. Given an onboarding interview, step-wise market context, and advisory dialogues, models must generate rankings over a fixed investment horizon. Crucially, Conv-FinRe provides multi-view references that distinguish descriptive behavior from normative utility grounded in investor-specific risk preferences, enabling diagnosis of whether an LLM follows rational analysis, mimics user noise, or is driven by market momentum. We build the benchmark from real market data and human decision trajectories, instantiate controlled advisory conversations, and evaluate a suite of state-of-the-art LLMs. Results reveal a persistent tension between rational decision quality and behavioral alignment: models that perform well on utility-based ranking often fail to match user choices, whereas behaviorally aligned models can overfit short-term noise. The dataset is publicly released on Hugging Face, and the codebase is available on GitHub.

