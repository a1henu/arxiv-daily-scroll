---
layout: default
title: X-AVDT: Audio-Visual Cross-Attention for Robust Deepfake Detection
---

# X-AVDT: Audio-Visual Cross-Attention for Robust Deepfake Detection
**arXiv**：[2603.08483v1](https://arxiv.org/abs/2603.08483) · [PDF](https://arxiv.org/pdf/2603.08483.pdf)  
**作者**：Youngseo Kim, Kwan Yun, Seokhyeon Hong, Sihun Cha, Colette Suhjung Koo, Junyong Noh  

**一句话要点**：提出X-AVDT，利用生成器内部音频-视觉交叉注意力进行鲁棒深度伪造检测

**关键词**：深度伪造检测, 音频-视觉交叉注意力, DDIM反转, 多模态数据集, 生成器内部信号

## 3 点简述
- 问题：高度逼真的合成视频增加恶意使用风险，现有检测器面临挑战
- 方法：通过DDIM反转提取视频复合信号和音频-视觉交叉注意力特征，暴露生成器内部对齐线索
- 效果：在MMDF数据集上领先，泛化至外部基准和未见生成器，准确率提升13.1%

## 摘要（原文）

> The surge of highly realistic synthetic videos produced by contemporary generative systems has significantly increased the risk of malicious use, challenging both humans and existing detectors. Against this backdrop, we take a generator-side view and observe that internal cross-attention mechanisms in these models encode fine-grained speech-motion alignment, offering useful correspondence cues for forgery detection. Building on this insight, we propose X-AVDT, a robust and generalizable deepfake detector that probes generator-internal audio-visual signals accessed via DDIM inversion to expose these cues. X-AVDT extracts two complementary signals: (i) a video composite capturing inversion-induced discrepancies, and (ii) an audio-visual cross-attention feature reflecting modality alignment enforced during generation. To enable faithful cross-generator evaluation, we further introduce MMDF, a new multimodal deepfake dataset spanning diverse manipulation types and rapidly evolving synthesis paradigms, including GANs, diffusion, and flow-matching. Extensive experiments demonstrate that X-AVDT achieves leading performance on MMDF and generalizes strongly to external benchmarks and unseen generators, outperforming existing methods with accuracy improved by 13.1%. Our findings highlight the importance of leveraging internal audio-visual consistency cues for robustness to future generators in deepfake detection.

