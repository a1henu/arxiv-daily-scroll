---
layout: default
title: Seeing What You Say: Expressive Image Generation from Speech
---

# Seeing What You Say: Expressive Image Generation from Speech
**arXiv**：[2511.03423v1](https://arxiv.org/abs/2511.03423) · [PDF](https://arxiv.org/pdf/2511.03423.pdf)  
**作者**：Jiyoung Lee, Song Park, Sanghyuk Chun, Soo-Whan Chung  

**一句话要点**：提出VoxStudio以从语音生成富有表现力的图像，联合对齐语言和副语言信息。

**关键词**：语音到图像生成, 端到端模型, 语音信息瓶颈, 情感语音图像数据集, 副语言信息对齐

## 3 点简述
- 核心问题：语音到图像生成中忽略语调、情感等副语言细节，导致表达性不足。
- 方法要点：使用语音信息瓶颈模块压缩语音为语义令牌，保留韵律和情感，实现端到端生成。
- 实验或效果：在多个基准测试中验证可行性，突出情感一致性和语言歧义等挑战。

## 摘要（原文）

> This paper proposes VoxStudio, the first unified and end-to-end
> speech-to-image model that generates expressive images directly from spoken
> descriptions by jointly aligning linguistic and paralinguistic information. At
> its core is a speech information bottleneck (SIB) module, which compresses raw
> speech into compact semantic tokens, preserving prosody and emotional nuance.
> By operating directly on these tokens, VoxStudio eliminates the need for an
> additional speech-to-text system, which often ignores the hidden details beyond
> text, e.g., tone or emotion. We also release VoxEmoset, a large-scale paired
> emotional speech-image dataset built via an advanced TTS engine to affordably
> generate richly expressive utterances. Comprehensive experiments on the
> SpokenCOCO, Flickr8kAudio, and VoxEmoset benchmarks demonstrate the feasibility
> of our method and highlight key challenges, including emotional consistency and
> linguistic ambiguity, paving the way for future research.

