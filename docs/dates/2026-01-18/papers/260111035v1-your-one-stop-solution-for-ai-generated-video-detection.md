---
layout: default
title: Your One-Stop Solution for AI-Generated Video Detection
---

# Your One-Stop Solution for AI-Generated Video Detection
**arXiv**：[2601.11035v1](https://arxiv.org/abs/2601.11035) · [PDF](https://arxiv.org/pdf/2601.11035.pdf)  
**作者**：Long Ma, Zihao Xue, Yan Wang, Zhiyuan Yan, Jin Xu, Xiaorui Jiang, Haiyang Yu, Yong Liao, Zhen Bi  

**一句话要点**：提出AIGVDBench基准以解决AI生成视频检测领域数据集与评估不足的问题。

**关键词**：AI生成视频检测, 基准构建, 数据集评估, 生成模型多样性, 检测器分析

## 3 点简述
- 核心问题：现有数据集规模小、模型过时，且基准缺乏系统性分析，阻碍检测方法发展。
- 方法要点：构建覆盖31个先进生成模型和44万视频的综合性基准，执行1500次评估。
- 实验或效果：通过8项深入分析和4个新发现，为未来研究提供基础，并开源基准。

## 摘要（原文）

> Recent advances in generative modeling can create remarkably realistic synthetic videos, making it increasingly difficult for humans to distinguish them from real ones and necessitating reliable detection methods.
>   However, two key limitations hinder the development of this field.
>   \textbf{From the dataset perspective}, existing datasets are often limited in scale and constructed using outdated or narrowly scoped generative models, making it difficult to capture the diversity and rapid evolution of modern generative techniques. Moreover, the dataset construction process frequently prioritizes quantity over quality, neglecting essential aspects such as semantic diversity, scenario coverage, and technological representativeness.
>   \textbf{From the benchmark perspective}, current benchmarks largely remain at the stage of dataset creation, leaving many fundamental issues and in-depth analysis yet to be systematically explored.
>   Addressing this gap, we propose AIGVDBench, a benchmark designed to be comprehensive and representative, covering \textbf{31} state-of-the-art generation models and over \textbf{440,000} videos. By executing more than \textbf{1,500} evaluations on \textbf{33} existing detectors belonging to four distinct categories. This work presents \textbf{8 in-depth analyses} from multiple perspectives and identifies \textbf{4 novel findings} that offer valuable insights for future research. We hope this work provides a solid foundation for advancing the field of AI-generated video detection.
>   Our benchmark is open-sourced at https://github.com/LongMa-2025/AIGVDBench.

