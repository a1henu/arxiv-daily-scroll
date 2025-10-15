---
layout: default
title: VideoLucy: Deep Memory Backtracking for Long Video Understanding
---

# VideoLucy: Deep Memory Backtracking for Long Video Understanding
**arXiv**：[2510.12422v1](https://arxiv.org/abs/2510.12422) · [PDF](https://arxiv.org/pdf/2510.12422.pdf)  
**作者**：Jialong Zuo, Yongtai Deng, Lingdong Kong, Jingkang Yang, Rui Jin, Yiwei Zhang, Nong Sang, Liang Pan, Ziwei Liu, Changxin Gao  

**一句话要点**：提出VideoLucy框架以解决长视频理解中的时序上下文和关键信息丢失问题

**关键词**：长视频理解, 分层记忆结构, 迭代回溯机制, EgoMem基准, 代理系统, 时序上下文建模

## 3 点简述
- 核心问题：现有基于LLM的代理系统难以捕捉连续帧的时序上下文，且稀疏采样易丢失关键信息
- 方法要点：采用分层记忆结构和迭代回溯机制，从粗到细挖掘视频全局的深度记忆
- 实验或效果：在多个基准测试中显著优于现有方法，性能超越GPT-4o等专有模型

## 摘要（原文）

> Recent studies have shown that agent-based systems leveraging large language
> models (LLMs) for key information retrieval and integration have emerged as a
> promising approach for long video understanding. However, these systems face
> two major challenges. First, they typically perform modeling and reasoning on
> individual frames, struggling to capture the temporal context of consecutive
> frames. Second, to reduce the cost of dense frame-level captioning, they adopt
> sparse frame sampling, which risks discarding crucial information. To overcome
> these limitations, we propose VideoLucy, a deep memory backtracking framework
> for long video understanding. Inspired by the human recollection process from
> coarse to fine, VideoLucy employs a hierarchical memory structure with
> progressive granularity. This structure explicitly defines the detail level and
> temporal scope of memory at different hierarchical depths. Through an
> agent-based iterative backtracking mechanism, VideoLucy systematically mines
> video-wide, question-relevant deep memories until sufficient information is
> gathered to provide a confident answer. This design enables effective temporal
> understanding of consecutive frames while preserving critical details. In
> addition, we introduce EgoMem, a new benchmark for long video understanding.
> EgoMem is designed to comprehensively evaluate a model's ability to understand
> complex events that unfold over time and capture fine-grained details in
> extremely long videos. Extensive experiments demonstrate the superiority of
> VideoLucy. Built on open-source models, VideoLucy significantly outperforms
> state-of-the-art methods on multiple long video understanding benchmarks,
> achieving performance even surpassing the latest proprietary models such as
> GPT-4o. Our code and dataset will be made publicly at
> https://videolucy.github.io

