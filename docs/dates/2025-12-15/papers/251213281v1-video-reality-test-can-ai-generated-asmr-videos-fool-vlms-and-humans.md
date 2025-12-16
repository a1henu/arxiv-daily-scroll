---
layout: default
title: Video Reality Test: Can AI-Generated ASMR Videos fool VLMs and Humans?
---

# Video Reality Test: Can AI-Generated ASMR Videos fool VLMs and Humans?
**arXiv**：[2512.13281v1](https://arxiv.org/abs/2512.13281) · [PDF](https://arxiv.org/pdf/2512.13281.pdf)  
**作者**：Jiaqi Wang, Weijia Wu, Yi Zhan, Rui Zhao, Ming Hu, James Cheng, Wei Liu, Philip Torr, Kevin Qinghong Lin  

**一句话要点**：提出Video Reality Test基准，评估AI生成ASMR视频在视听耦合下欺骗人类和视觉语言模型的能力。

**关键词**：AI生成视频检测, 视听一致性, ASMR视频基准, 对抗性评估, 视觉语言模型, 感知真实性

## 3 点简述
- 核心问题：AI生成视频的感知真实性，尤其在视听同步的沉浸式场景中，能否可靠欺骗人类和模型。
- 方法要点：基于真实ASMR视频构建基准，采用对抗性创作者-评审者协议，测试视频生成模型与视觉语言模型的交互。
- 实验或效果：最佳生成模型Veo3.1-Fast在欺骗视觉语言模型方面表现突出，但人类专家识别准确率更高，音频提升鉴别但水印等表面线索仍误导模型。

## 摘要（原文）

> Recent advances in video generation have produced vivid content that are often indistinguishable from real videos, making AI-generated video detection an emerging societal challenge. Prior AIGC detection benchmarks mostly evaluate video without audio, target broad narrative domains, and focus on classification solely. Yet it remains unclear whether state-of-the-art video generation models can produce immersive, audio-paired videos that reliably deceive humans and VLMs. To this end, we introduce Video Reality Test, an ASMR-sourced video benchmark suite for testing perceptual realism under tight audio-visual coupling, featuring the following dimensions: \textbf{(i) Immersive ASMR video-audio sources.} Built on carefully curated real ASMR videos, the benchmark targets fine-grained action-object interactions with diversity across objects, actions, and backgrounds. \textbf{(ii) Peer-Review evaluation.} An adversarial creator-reviewer protocol where video generation models act as creators aiming to fool reviewers, while VLMs serve as reviewers seeking to identify fakeness. Our experimental findings show: The best creator Veo3.1-Fast even fools most VLMs: the strongest reviewer (Gemini 2.5-Pro) achieves only 56\% accuracy (random 50\%), far below that of human experts (81.25\%). Adding audio improves real-fake discrimination, yet superficial cues such as watermarks can still significantly mislead models. These findings delineate the current boundary of video generation realism and expose limitations of VLMs in perceptual fidelity and audio-visual consistency. Our code is available at https://github.com/video-reality-test/video-reality-test.

