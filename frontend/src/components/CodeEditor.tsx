interface Props {
  value: string;
  onChange: (v: string) => void;
}

export default function CodeEditor({ value, onChange }: Props) {
  return (
    <textarea
      value={value}
      onChange={e => onChange(e.target.value)}
      rows={15}
      style={{ width: "100%", fontFamily: "monospace" }}
    />
  );
}
