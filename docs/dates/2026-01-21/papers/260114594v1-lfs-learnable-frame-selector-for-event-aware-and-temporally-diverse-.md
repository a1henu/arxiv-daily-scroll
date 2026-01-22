---
layout: default
title: LFS: Learnable Frame Selector for Event-Aware and Temporally Diverse Video Captioning
---

# LFS: Learnable Frame Selector for Event-Aware and Temporally Diverse Video Captioning
**arXiv**：[2601.14594v1](https://arxiv.org/abs/2601.14594) · [PDF](https://arxiv.org/pdf/2601.14594.pdf)  
**作者**：Lianying Chao, Linfeng Yin, Peiyu Ren, Yifan Jiang, Qiaoyu Ren, Dingcheng Shan, Jing-cheng Pang, Sijie Wu, Xubin Li, Kai Zhang  

**一句话要点**：提出可学习帧选择器以解决视频描述中事件感知与时间多样性的问题

**关键词**：视频描述, 帧选择, 事件感知, 时间多样性, LLM优化, 数据集构建

## 3 点简述
- 视频描述中均匀采样忽略事件分布不均，导致描述质量受限
- LFS通过建模时间重要性平衡多样性与相关性，并利用冻结LLM的反馈优化选择
- 在多个基准测试中提升描述质量，并引入新数据集ICH-CC以贴近人类认知

## 摘要（原文）

> Video captioning models convert frames into visual tokens and generate descriptions with large language models (LLMs). Since encoding all frames is prohibitively expensive, uniform sampling is the default choice, but it enforces equal temporal coverage while ignoring the uneven events distribution. This motivates a Learnable Frame Selector (LFS) that selects temporally diverse and event-relevant frames. LFS explicitly models temporal importance to balance temporal diversity and event relevance, and employs a stratified strategy to ensure temporal coverage while avoiding clustering. Crucially, LFS leverages caption feedback from frozen video-LLMs to learn frame selection that directly optimizes downstream caption quality. Additionally, we identify the gap between existing benchmark and human's cognition. Thus, we introduce ICH-CC built from carefully designed questions by annotators that reflect human-consistent understanding of video. Experiments indicate that LFS consistently improves detailed video captioning across two representative community benchmarks and ICH-CC, achieving up to 2.0% gains on VDC and over 4% gains on ICH-CC. Moreover, we observe that enhanced captions with LFS leads to improved performance on video question answering. Overall, LFS provides an effective and easy-to-integrate solution for detailed video captioning.

