---
layout: default
title: Omni-Captioner: Data Pipeline, Models, and Benchmark for Omni Detailed Perception
---

# Omni-Captioner: Data Pipeline, Models, and Benchmark for Omni Detailed Perception
**arXiv**：[2510.12720v1](https://arxiv.org/abs/2510.12720) · [PDF](https://arxiv.org/pdf/2510.12720.pdf)  
**作者**：Ziyang Ma, Ruiyang Xu, Zhenghao Xing, Yunfei Chu, Yuxuan Wang, Jinzheng He, Jin Xu, Pheng-Ann Heng, Kai Yu, Junyang Lin, Eng Siong Chng, Xie Chen  

**一句话要点**：提出Omni-Captioner数据管道与模型，以解决全模态细粒度感知中的细节与幻觉问题。

**关键词**：全模态感知, 细粒度描述, 数据生成管道, 音频-视觉模型, 基准评估

## 3 点简述
- 核心问题：当前全模态语言模型在细粒度感知中存在细节与幻觉共增长问题。
- 方法要点：开发Omni-Detective数据生成管道，自动产生高细节、低幻觉的多模态数据。
- 实验或效果：Omni-Captioner在多个基准测试中达到最优或最佳平衡性能。

## 摘要（原文）

> Fine-grained perception of multimodal information is critical for advancing
> human-AI interaction. With recent progress in audio-visual technologies, Omni
> Language Models (OLMs), capable of processing audio and video signals in
> parallel, have emerged as a promising paradigm for achieving richer
> understanding and reasoning. However, their capacity to capture and describe
> fine-grained details remains limited explored. In this work, we present a
> systematic and comprehensive investigation of omni detailed perception from the
> perspectives of the data pipeline, models, and benchmark. We first identify an
> inherent "co-growth" between detail and hallucination in current OLMs. To
> address this, we propose Omni-Detective, an agentic data generation pipeline
> integrating tool-calling, to autonomously produce highly detailed yet minimally
> hallucinatory multimodal data. Based on the data generated with Omni-Detective,
> we train two captioning models: Audio-Captioner for audio-only detailed
> perception, and Omni-Captioner for audio-visual detailed perception. Under the
> cascade evaluation protocol, Audio-Captioner achieves the best performance on
> MMAU and MMAR among all open-source models, surpassing Gemini 2.5 Flash and
> delivering performance comparable to Gemini 2.5 Pro. On existing detailed
> captioning benchmarks, Omni-Captioner sets a new state-of-the-art on VDC and
> achieves the best trade-off between detail and hallucination on the
> video-SALMONN 2 testset. Given the absence of a dedicated benchmark for omni
> detailed perception, we design Omni-Cloze, a novel cloze-style evaluation for
> detailed audio, visual, and audio-visual captioning that ensures stable,
> efficient, and reliable assessment. Experimental results and analysis
> demonstrate the effectiveness of Omni-Detective in generating high-quality
> detailed captions, as well as the superiority of Omni-Cloze in evaluating such
> detailed captions.

